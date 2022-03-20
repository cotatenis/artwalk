from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleAdidasSuperStarSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-adidas-superstar'
    start_urls = ["https://www.artwalk.com.br/adidas-superstar-feminino?O=OrderByPriceASC&PS=24"]