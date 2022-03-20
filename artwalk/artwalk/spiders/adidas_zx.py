from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from collections import Counter
from parsel import Selector
from typing import Tuple, List
from time import sleep
class ArtWalkAdidasZXSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-adidas-zx'
    start_urls = [
        'https://www.artwalk.com.br/masculino/calcados/adidas%20ZX?O=OrderByReleaseDateDESC&PS=24'
    ]
    href_counter = Counter([start_urls[0]])
    def start_requests(self):
        for url in self.start_urls:
            yield SeleniumRequest(
                url=url, 
                callback=self.middle, 
            )

    def middle(self, response):
        products_href, _ = self.paginate(response=response)
        while self.href_counter.most_common(1)[0][1] < 3:
            products_href, _ = self.paginate(response=response)
            self.check_duplicates(products_href=products_href)
        for url in set(products_href):
            self.logger.debug(f"Preparando GET para a url: {url}")
            yield SeleniumRequest(url=url, callback=self.parse_product_page)

    def check_duplicates(self, products_href: List[str]):
        for href in products_href:
            self.href_counter.update([href])

    def paginate(self, response) -> Tuple[list, int]:
        products, num_products = self.load_new_products(response=response)
        sleep(.5)
        self.close_notifications_banner(response=response)  
        sleep(.5)
        self.move_screen_to_pagination_btn(response=response)
        sleep(.5)
        self.click_pagination_btn(response=response)
        return products, num_products


    def load_new_products(self, response) -> Tuple[list, int]:
        sel = Selector(text=response.request.meta['driver'].page_source)
        products = sel.xpath("//div[@class='product-item-container']/a/@href").getall()
        num_products = len(products)
        self.logger.debug(f"Número de produtos na página {num_products}")
        return products, num_products