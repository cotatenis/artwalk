from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleNikeLebronSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-nike-lebron'
    start_urls = ["https://www.artwalk.com.br/nike-lebron?O=OrderByPriceASC&PS=24"]