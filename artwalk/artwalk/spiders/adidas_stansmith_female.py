from artwalk.spiders.adidas_originals_female import ArtWalkFemaleAdidasOriginalsSpider

class ArtWalkFemaleAdidasStanSmithSpider(ArtWalkFemaleAdidasOriginalsSpider):
    name = 'artwalk-female-adidas-stansmith'
    start_urls = ["https://www.artwalk.com.br/adidas-stan-smith?O=OrderByPriceASC&PS=24"]