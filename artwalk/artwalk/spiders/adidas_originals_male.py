from scrapy import Request, Spider
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from parsel import Selector
from typing import Tuple
from artwalk.items import ArtwalkAdidasItem
from scrapy.utils.project import get_project_settings

class ArtWalkAMaleAdidasOriginalsSpider(Spider):
    name = 'artwalk-male-adidas-originals'
    allowed_domains = ['artwalk.com.br']
    start_urls = [
        #adidas originals
        'https://www.artwalk.com.br/adidas-originals?PS=24&amp;O=OrderByReleaseDateDESC',
    ]
    settings = get_project_settings()
    version = settings.get("VERSION")
    def start_requests(self):
        for url in self.start_urls:
            masculino_filter = "//div[@class='search-single-navigator']/h3[@class='masculino']"
            yield SeleniumRequest(
                url=url, 
                callback=self.middle, 
                wait_time=5,
                wait_until=EC.element_to_be_clickable((By.XPATH, masculino_filter))
            )
    def middle(self, response):
        ##male, female, children
        shoes_per_genre_href = response.xpath("//a[@title='Calçados']/@href").getall()
        shoes_qty = response.xpath("//a[@title='Calçados']/text()").re(r"\d+")
        male_href = shoes_per_genre_href[0]
        male_qty = shoes_qty[0]
        yield SeleniumRequest(url=male_href, callback=self.parse_pages, cb_kwargs={"quantity" : male_qty})
    
    def parse_pages(self,response, quantity):
        #first page
        href_products = ""
        self.close_windows_from_landpage(response=response)
        qty_product = int(quantity)*2
        num_products = 0
        while num_products < qty_product:
            href_products, num_products = self.paginate(response=response)
            sleep(1)
        if href_products:
            for url in href_products:
                self.logger.debug(f"Preparando GET para a url: {url}")
                yield SeleniumRequest(url=url, callback=self.parse_product_page)

    def parse_product_page(self, response):
        raw_sku_id = response.xpath("//input[@id='___rc-p-sku-ids']/@value").get()
        imgs_urls = response.selector.xpath("//li[@class = 'ns-product-image']/img/@src|//li[@class='ns-product-image is-selected']/img/@src").getall()
        if raw_sku_id:
            sku_id = raw_sku_id.split(",")[0]
            headers = {
                "authority": "www.artwalk.com.br",
                "pragma": "no-cache",
                "cache-control": "no-cache",
                "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
                "accept": "*/*",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "referer": response.url,
                "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
            }
            self.logger.debug(f"Preparando chamada para o endpoint: {sku_id}")
            url = f'https://www.artwalk.com.br/api/catalog_system/pub/products/search?&fq=skuId:{sku_id}'
            reference_first_image = imgs_urls[0].split("/")[-1].split("?")[-2]
            yield Request(url=url, method='GET', dont_filter=True, headers=headers, callback=self.parse, priority=1, cb_kwargs={'image_urls' : imgs_urls, 'reference_first_image' : reference_first_image})


    def parse(self, response, image_urls: list, reference_first_image):
        if not reference_first_image:
            raise ValueError()
        data = self.parse_item(response=response)
        if data:
            data['image_urls'] = image_urls
            brand = data.get('brand', None)
            if brand != "Nike":
                usku = data['productReference'].replace("-","")[:6]
            else:
                raw_usku = data.get('productReference')
                raw_usku = raw_usku.split("-")
                usku = raw_usku[0]+raw_usku[1]+"-"+raw_usku[2]
            data['sku'] = usku
            data['reference_first_image'] = f"{usku}_{reference_first_image}"
            data['image_uris'] =  [f"{self.settings.get('IMAGES_STORE')}{usku}_{filename.split('/')[-1].split('?')[0]}" for filename in image_urls]
            yield data

    def parse_item(self, response):
        data = response.json()
        if data:
            rawdata = data[0]
            tipo_produto = rawdata.get("Tipo de Produto", None)
            if tipo_produto:
                del rawdata['Tipo de Produto']
                rawdata['TipodeProduto'] = tipo_produto
            lancamento_calendario = rawdata.get("Lançto Calendário", None)
            if lancamento_calendario:
                del rawdata['Lançto Calendário']
                rawdata['LanctoCalendario'] = lancamento_calendario
            cod_ref_multi_var =  rawdata.get("Cod. Ref. Multi Var.", None)
            if cod_ref_multi_var:
                del rawdata['Cod. Ref. Multi Var.']
                rawdata['CodRefMultiVar'] = cod_ref_multi_var
            cod_ref_variacao = rawdata.get("Cod. Ref. Variação", None)
            if cod_ref_variacao:
                del rawdata['Cod. Ref. Variação']
                rawdata['CodRefVariacao'] = cod_ref_variacao
            lancamento_mundial = rawdata.get("Lançto Mundial", None)
            if lancamento_mundial:
                del rawdata['Lançto Mundial']
                rawdata['LanctoMundial'] = lancamento_mundial 
            black_friday = rawdata.get("Black Friday", None)
            if black_friday:
                del rawdata['Black Friday']
                rawdata['BlackFriday'] = black_friday
            rawdata['spider_version'] = self.version
            rawdata['spider'] = self.name
            if set(rawdata.keys()).difference(set(ArtwalkAdidasItem.fields.keys())):
                return rawdata
            else:
                return ArtwalkAdidasItem(**rawdata)
        return None

    def close_localization_banner(self, response):
        try:
            localization_addr = response.request.meta['driver'].find_element_by_xpath("//button[@id='ModalAlterarLocalizacaoFechar']")
        except NoSuchElementException:
            pass
        else:
            sleep(1)
            response.request.meta['driver'].execute_script("arguments[0].click();", localization_addr)
    
    def close_terms_of_service(self, response):
        try:
            accept_close = response.request.meta['driver'].find_element_by_xpath("//button[@class='acept-close']")
        except NoSuchElementException:
            pass
        else:
            sleep(1)
            response.request.meta['driver'].execute_script("arguments[0].click();", accept_close)



    def close_notifications_banner(self, response):
        try:
            allow_notifcations_close = response.request.meta['driver'].find_element_by_xpath("//button[@class='shoppush-prompt-close']")
        except NoSuchElementException:
            pass
        else:
            sleep(1)
            response.request.meta['driver'].execute_script("arguments[0].click();", allow_notifcations_close)
    
    def move_screen_to_pagination_btn(self, response):
        try:
            next_page = response.request.meta['driver'].find_element_by_xpath("//span[@class='ns-button__text']")
        except NoSuchElementException:
            sleep(5)
            next_page = response.request.meta['driver'].find_element_by_xpath("//span[@class='ns-button__text']")
        else:
            actions = ActionChains(response.request.meta['driver'])
            actions.move_to_element(next_page).perform()
    
    def click_pagination_btn(self, response):
        next_page = response.request.meta['driver'].find_element_by_xpath("//span[@class='ns-button__text']")
        try:
            response.request.meta['driver'].execute_script("arguments[0].click();", next_page)
        except NoSuchElementException:
            pass
        else:
            return None

    def load_new_products(self, response) -> Tuple[list, int]:
        sel = Selector(text=response.request.meta['driver'].page_source)
        products = sel.xpath("//div[@class='product-item-container']/a/@href").getall()
        num_products = len(products)
        self.logger.debug(f"Número de produtos na página {num_products}")
        return products, num_products
    
    def paginate(self, response) -> Tuple[list, int]:
        products, num_products = self.load_new_products(response=response)
        sleep(.5)
        self.close_notifications_banner(response=response)  
        sleep(.5)
        self.move_screen_to_pagination_btn(response=response)
        sleep(.5)
        self.click_pagination_btn(response=response)
        return products, num_products

    def close_windows_from_landpage(self, response):
        self.close_localization_banner(response=response)
        self.close_notifications_banner(response=response)        
        self.close_terms_of_service(response=response)