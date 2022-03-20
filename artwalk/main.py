from scrapy.utils.project import get_project_settings
import os
from scrapy.crawler import CrawlerRunner
from artwalk.spiders import (
    ArtWalkAMaleAdidasOriginalsSpider,
    ArtWalkFemaleAdidasOriginalsSpider,
    ArtWalkKidsAdidasOriginalsSpider,
    ArtWalkMaleAdidasStanSmithSpider,
    ArtWalkFemaleAdidasStanSmithSpider,
    ArtWalkKidsAdidasStanSmithSpider,
    ArtWalkMaleAdidasSuperStarSpider,
    ArtWalkFemaleAdidasSuperStarSpider,
    ArtWalkKidsAdidasSuperStarSpider,
    ArtWalkAdidasZXSpider,
    ArtWalkAdidasIvyParkSpider,
    ArtWalkFemaleNikeAF1Spider,
    ArtWalkMaleNikeAF1Spider,
    ArtWalkFemaleNikeAirMaxSpider,
    ArtWalkMaleNikeAirMaxSpider,
    ArtWalkFemaleNikeJordanSpider,
    ArtWalkMaleNikeJordanSpider,
    ArtWalkFemaleNikeLebronSpider,
    ArtWalkMaleNikeLebronSpider,
    ArtWalkKidsNikeLebronSpider,
    ArtWalkFemaleNikeSpider,
    ArtWalkMaleNikeSpider,
    ArtWalkKidsNikeSpider
)
from scrapy.utils.log import configure_logging
from config import settings
from typer import Typer
from twisted.internet import reactor
import os

app = Typer()

@app.command()
def start_crawl(brand: str = ""):
    if brand not in settings.get("store.brands"):
        raise ValueError(f"{brand} is not a valid store.")
    spider = {
        'artwalk-male-adidas-originals' : ArtWalkAMaleAdidasOriginalsSpider,
        'artwalk-female-adidas-originals' : ArtWalkFemaleAdidasOriginalsSpider,
        'artwalk-kids-adidas-originals' : ArtWalkKidsAdidasOriginalsSpider,
        'artwalk-male-adidas-stansmith' : ArtWalkMaleAdidasStanSmithSpider,
        'artwalk-female-adidas-stansmith' : ArtWalkFemaleAdidasStanSmithSpider,
        'artwalk-kids-adidas-stansmith' : ArtWalkKidsAdidasStanSmithSpider,
        'artwalk-male-adidas-superstar' : ArtWalkMaleAdidasSuperStarSpider,
        'artwalk-female-adidas-superstar' : ArtWalkFemaleAdidasSuperStarSpider,
        'artwalk-kids-adidas-superstar' : ArtWalkKidsAdidasSuperStarSpider,
        'artwalk-adidas-zx' : ArtWalkAdidasZXSpider,
        'artwalk-adidas-ivypark' : ArtWalkAdidasIvyParkSpider,
        'artwalk-female-nike-af1' : ArtWalkFemaleNikeAF1Spider,
        'artwalk-male-nike-af1' : ArtWalkMaleNikeAF1Spider,
        'artwalk-male-nike-airmax' : ArtWalkMaleNikeAirMaxSpider,
        'artwalk-female-nike-airmax' : ArtWalkFemaleNikeAirMaxSpider,
        'artwalk-female-nike-jordan' : ArtWalkFemaleNikeJordanSpider,
        'artwalk-male-nike-jordan' : ArtWalkMaleNikeJordanSpider,
        'artwalk-female-nike-lebron' : ArtWalkFemaleNikeLebronSpider,
        'artwalk-male-nike-lebron' : ArtWalkMaleNikeLebronSpider,
        'artwalk-kids-nike-lebron'  : ArtWalkKidsNikeLebronSpider,
        'artwalk-female-nike' : ArtWalkFemaleNikeSpider,
        'artwalk-male-nike' : ArtWalkMaleNikeSpider,
        'artwalk-kids-nike' : ArtWalkKidsNikeSpider
}
    crawl_settings = get_project_settings()
    settings_module_path = os.environ.get("SCRAPY_ENV", "artwalk.settings")
    crawl_settings.setmodule(settings_module_path)
    configure_logging(crawl_settings)
    runner = CrawlerRunner(crawl_settings)
    d = runner.crawl(spider[brand])
    d.addBoth(lambda _: reactor.stop())
    reactor.run() 


if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = settings.get("store.GOOGLE_APPLICATION_CREDENTIALS", "./credentials/credentials.json")
    app()
