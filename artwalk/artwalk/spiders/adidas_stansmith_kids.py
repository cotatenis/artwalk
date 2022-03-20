from artwalk.spiders.adidas_originals_kids import ArtWalkKidsAdidasOriginalsSpider

class ArtWalkKidsAdidasStanSmithSpider(ArtWalkKidsAdidasOriginalsSpider):
    name = 'artwalk-kids-adidas-stansmith'
    start_urls = ["https://www.artwalk.com.br/adidas-stan-smith?O=OrderByPriceASC&PS=24"]