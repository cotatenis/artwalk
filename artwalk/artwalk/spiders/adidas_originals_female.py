from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider
from scrapy_selenium import SeleniumRequest

class ArtWalkFemaleAdidasOriginalsSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-female-adidas-originals'
    def middle(self, response):
        ##male, female, children
        shoes_per_genre_href = response.xpath("//a[@title='Calçados']/@href").getall()
        shoes_qty = response.xpath("//a[@title='Calçados']/text()").re(r"\d+")
        female_href = shoes_per_genre_href[1]
        female_qty = shoes_qty[1]
        yield SeleniumRequest(url=female_href, callback=self.parse_pages, cb_kwargs={"quantity" : female_qty})
