from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleNikeAF1Spider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-nike-af1'
    start_urls = ["https://www.artwalk.com.br/nike-air-force?O=OrderByPriceASC&PS=24"]