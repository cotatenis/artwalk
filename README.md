
░█████╗░░█████╗░████████╗░█████╗░████████╗███████╗███╗░░██╗██╗░██████╗
██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝████╗░██║██║██╔════╝
██║░░╚═╝██║░░██║░░░██║░░░███████║░░░██║░░░█████╗░░██╔██╗██║██║╚█████╗░
██║░░██╗██║░░██║░░░██║░░░██╔══██║░░░██║░░░██╔══╝░░██║╚████║██║░╚═══██╗
╚█████╔╝╚█████╔╝░░░██║░░░██║░░██║░░░██║░░░███████╗██║░╚███║██║██████╔╝
░╚════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═╝╚═════╝░


--------------------------------------------------------------------------

# Web crawler

url: [https://www.artwalk.com.br/](https://www.artwalk.com.br/)

# 1. Configuration
Before you run this project and for the proper running of this program you need to set up some variables inside `artwalk/artwalk/settings.py`.
## 1.1 SENTRY
This project utilizes [SENTRY](https://sentry.io/) for error tracking.

- `SENTRY_DSN`
- `SPIDERMON_SENTRY_PROJECT_NAME`
- `SPIDERMON_SENTRY_ENVIRONMENT_TYPE`

## 1.2 GOOGLE CLOUD PLATFORM

- `GCS_PROJECT_ID` 
- `GCP_CREDENTIALS`
- `GCP_STORAGE`
- `GCP_STORAGE_CRAWLER_STATS`
- `IMAGES_STORE`

## 1.3 DISCORD
- `DISCORD_WEBHOOK_URL`
- `DISCORD_THUMBNAIL_URL`
- `SPIDERMON_DISCORD_WEBHOOK_URL`

# 2. Implemented Brands
- artwalk-male-adidas-originals [`ArtWalkAMaleAdidasOriginalsSpider`]
- artwalk-female-adidas-originals [`ArtWalkFemaleAdidasOriginalsSpider`]
- artwalk-kids-adidas-originals [`ArtWalkKidsAdidasOriginalsSpider`]
- artwalk-male-adidas-stansmith [`ArtWalkMaleAdidasStanSmithSpider`]
- artwalk-female-adidas-stansmith [`ArtWalkFemaleAdidasStanSmithSpider`]
- artwalk-kids-adidas-stansmith [`ArtWalkKidsAdidasStanSmithSpider`]
- artwalk-male-adidas-superstar [`ArtWalkMaleAdidasSuperStarSpider`]
- artwalk-female-adidas-superstar [`ArtWalkFemaleAdidasSuperStarSpider`]
- artwalk-kids-adidas-superstar [`ArtWalkKidsAdidasSuperStarSpider`]
- artwalk-adidas-zx [`ArtWalkAdidasZXSpider`]
- artwalk-adidas-ivypark [`ArtWalkAdidasIvyParkSpider`]
- artwalk-female-nike-af1 [`ArtWalkFemaleNikeAF1Spider`]
- artwalk-male-nike-af1 [`ArtWalkMaleNikeAF1Spider`]
- artwalk-male-nike-airmax [`ArtWalkMaleNikeAirMaxSpider`]
- artwalk-female-nike-airmax [`ArtWalkFemaleNikeAirMaxSpider`]
- artwalk-female-nike-jordan [`ArtWalkFemaleNikeJordanSpider`]
- artwalk-male-nike-jordan [`ArtWalkMaleNikeJordanSpider`]
- artwalk-female-nike-lebron [`ArtWalkFemaleNikeLebronSpider`]
- artwalk-male-nike-lebron [`ArtWalkMaleNikeLebronSpider`]
- artwalk-kids-nike-lebron [`ArtWalkKidsNikeLebronSpider`]
- artwalk-female-nike [`ArtWalkFemaleNikeSpider`]
- artwalk-male-nike [`ArtWalkMaleNikeSpider`]
- artwalk-kids-nike [`ArtWalkKidsNikeSpider`]

# 3. Build

```shell
cd artwalk
make docker-build-production
```

# 4. Publish

```shell
make docker-publish-production
```

# 5. Use
The parameter `brand` could receive one of the following values: [`artwalk-male-adidas-originals`, `artwalk-female-adidas-originals`, `artwalk-kids-adidas-originals`, `artwalk-male-adidas-stansmith`, `artwalk-female-adidas-stansmith`, `artwalk-kids-adidas-stansmith`, `artwalk-male-adidas-superstar`, `artwalk-female-adidas-superstar`, `artwalk-kids-adidas-superstar`, `artwalk-adidas-zx`, `artwalk-adidas-ivypark`, `artwalk-female-nike-af1`, `artwalk-male-nike-af1`, `artwalk-male-nike-airmax`, `artwalk-female-nike-airmax`, `artwalk-female-nike-jordan`, `artwalk-male-nike-jordan`, `artwalk-female-nike-lebron`, `artwalk-male-nike-lebron`, `artwalk-kids-nike-lebron`, `artwalk-female-nike`, `artwalk-male-nike`, `artwalk-kids-nike`].

```shell
docker run --shm-size="2g" gcr.io/cotatenis/cotatenis-crawl-artwalk:0.6.0 --brand=artwalk-adidas-zx
```
