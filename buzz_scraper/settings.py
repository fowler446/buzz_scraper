BOT_NAME = 'buzz_scraper'

SPIDER_MODULES = ['buzz_scraper.spiders']
NEWSPIDER_MODULE = 'buzz_scraper.spiders'
ITEM_PIPELINES = {
	'buzz_scraper.pipelines.MongoDBPipeline': 0,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "buzzfeed"
MONGODB_COLLECTION = "posts"

