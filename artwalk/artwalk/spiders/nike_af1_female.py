from artwalk.spiders.nike_jordan_male import ArtWalkMaleNikeJordanSpider
from scrapy_selenium import SeleniumRequest

class ArtWalkFemaleNikeAF1Spider(ArtWalkMaleNikeJordanSpider):
    name = 'artwalk-female-nike-af1'
    start_urls = ["https://www.artwalk.com.br/nike-air-force?O=OrderByPriceASC&PS=24"]
    def middle(self, response):
        ##male, female, children
        shoes_per_genre_href = response.xpath("//a[@title='Calçados']/@href").getall()
        shoes_qty = response.xpath("//a[@title='Calçados']/text()").re(r"\d+")
        female_href = shoes_per_genre_href[1]
        female_qty = shoes_qty[1]
        yield SeleniumRequest(url=female_href, callback=self.parse_pages, cb_kwargs={"quantity" : female_qty})