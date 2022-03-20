from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleNikeAirMaxSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-nike-airmax'
    start_urls = ["https://www.artwalk.com.br/nike-air-max?O=OrderByPriceASC&PS=24"]


