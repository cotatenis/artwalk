from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleNikeSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-nike'
    start_urls = ["https://www.artwalk.com.br/nike/T%C3%AAnis?PS=24&O=OrderByReleaseDateDESC"]


