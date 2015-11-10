BOT_NAME = 'wggesucht'

SPIDER_MODULES = ['scraper_app.spiders']

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'dima',
    'password': '123',
    'database': 'wggesucht'
}

ITEM_PIPELINES = ['scraper_app.pipelines.WGGesuchtPipeline']