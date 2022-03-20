from artwalk.spiders.adidas_originals_female import ArtWalkFemaleAdidasOriginalsSpider

class ArtWalkFemaleAdidasSuperStarSpider(ArtWalkFemaleAdidasOriginalsSpider):
    name = 'artwalk-female-adidas-superstar'
    start_urls = ["https://www.artwalk.com.br/adidas-superstar-feminino?O=OrderByPriceASC&PS=24"]