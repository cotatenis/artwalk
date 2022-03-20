from artwalk.spiders.adidas_originals_kids import ArtWalkKidsAdidasOriginalsSpider

class ArtWalkKidsAdidasSuperStarSpider(ArtWalkKidsAdidasOriginalsSpider):
    name = 'artwalk-kids-adidas-superstar'
    start_urls = ["https://www.artwalk.com.br/adidas-superstar-feminino?O=OrderByPriceASC&PS=24"]