from shutil import which
BOT_NAME = 'artwalk'
VERSION = "0-6-0"
SPIDER_MODULES = ['artwalk.spiders']
NEWSPIDER_MODULE = 'artwalk.spiders'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = which('chromedriver')
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # '--headless' if using chrome instead of firefox
DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800
}
MAGIC_FIELDS = {
    "timestamp": "$isotime",
    "spider": "$spider:name",
    "url": "$response:url",
}
SPIDER_MIDDLEWARES = {
    "scrapy_magicfields.MagicFieldsMiddleware": 100,
}
SPIDERMON_ENABLED = True
EXTENSIONS = {
    'artwalk.extensions.SentryLogging' : -1,
    'spidermon.contrib.scrapy.extensions.Spidermon': 500,
}
ITEM_PIPELINES = {
    "artwalk.pipelines.DiscordMessenger" : 100,
    "artwalk.pipelines.ArtWalkImagePipeline" : 200,
    "artwalk.pipelines.GCSPipeline": 300,
}
SPIDERMON_SPIDER_CLOSE_MONITORS = (
'artwalk.monitors.SpiderCloseMonitorSuite',
)

SPIDERMON_VALIDATION_DROP_ITEMS_WITH_ERRORS = False
SPIDERMON_PERIODIC_MONITORS = {
'artwalk.monitors.PeriodicMonitorSuite': 30, # time in seconds
}
SPIDERMON_CUSTOM_MIN_ITEMS = {
    'artwalk-male-adidas-originals' : 300,
    'artwalk-adidas-ivypark' : 1,
    'artwalk-female-adidas-originals' : 200,
    'artwalk-kids-adidas-originals' : 5,
    'artwalk-female-adidas-stansmith' : 7,
    'artwalk-kids-adidas-stansmith' : 1,
    'artwalk-female-adidas-stansmith' : 10,
    'artwalk-male-adidas-stansmith' : 5,
    'artwalk-female-adidas-superstar' : 200,
    'artwalk-kids-adidas-superstar' : 2,
    'artwalk-male-adidas-superstar' : 40,
    'artwalk-adidas-zx' : 40,
    'artwalk-male-nike-jordan' : 130,
    'artwalk-female-nike-jordan' : 10,
    'artwalk-male-nike-af1' : 90,
    'artwalk-female-nike-af1' : 40,
    'artwalk-male-nike-airmax' : 5,
    'artwalk-female-nike-airmax' : 80,
    'artwalk-male-nike-lebron' : 45,
    'artwalk-female-nike-lebron' : 10,
    'artwalk-kids-nike-lebron' : 4,
    'artwalk-male-nike' : 750,
    'artwalk-female-nike' : 250,
    'artwalk-kids-nike' : 15,
}
SENTRY_DSN = ""
SPIDERMON_SENTRY_PROJECT_NAME = ""
SPIDERMON_SENTRY_ENVIRONMENT_TYPE = ""
#THROTTLE
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 2
AUTOTHROTTLE_MAX_DELAY = 5

#GCP
GCS_PROJECT_ID = ""
GCP_CREDENTIALS = ""
GCP_STORAGE = ""
GCP_STORAGE_CRAWLER_STATS = ""
#FOR IMAGE UPLOAD
IMAGES_STORE = ""
IMAGES_THUMBS = {
    '400_400': (400, 400),
}
#DISCORD
DISCORD_WEBHOOK_URL = ""
DISCORD_THUMBNAIL_URL = ""
SPIDERMON_DISCORD_WEBHOOK_URL = ""

#LOGGING
LOG_LEVEL = 'INFO'