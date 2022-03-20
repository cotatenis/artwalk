from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleNikeJordanSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-nike-jordan'
    start_urls = ["https://www.artwalk.com.br/T%C3%AAnis/Jordan?O=OrderByReleaseDateDESC&&PS=24&map=specificationFilter_16,specificationFilter_15"]


