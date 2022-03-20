from artwalk.spiders.adidas_zx import ArtWalkAdidasZXSpider

class ArtWalkAdidasIvyParkSpider(ArtWalkAdidasZXSpider):
    name = 'artwalk-adidas-ivypark'
    start_urls = ["https://www.artwalk.com.br/T%C3%AAnis/811?O=OrderByPriceDESC&PS=24&map=specificationFilter_16,productClusterIds"]