from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider
from scrapy_selenium import SeleniumRequest

class ArtWalkKidsAdidasOriginalsSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-kids-adidas-originals'
    def middle(self, response):
        ##male, female, children
        shoes_per_genre_href = response.xpath("//a[@title='Calçados']/@href").getall()
        shoes_qty = response.xpath("//a[@title='Calçados']/text()").re(r"\d+")
        kids_href = shoes_per_genre_href[2]
        kids_qty = shoes_qty[2]
        yield SeleniumRequest(url=kids_href, callback=self.parse_pages, cb_kwargs={"quantity" : kids_qty})
