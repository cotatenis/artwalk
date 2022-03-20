from artwalk.spiders.adidas_originals_male import ArtWalkAMaleAdidasOriginalsSpider

class ArtWalkMaleAdidasStanSmithSpider(ArtWalkAMaleAdidasOriginalsSpider):
    name = 'artwalk-male-adidas-stansmith'
    start_urls = ["https://www.artwalk.com.br/adidas-stan-smith?O=OrderByPriceASC&PS=24"]