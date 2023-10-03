from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
      
if (Path(str(BASE_DIR / '.env')).is_file()):
    env.read_env(str(BASE_DIR / '.env'))

BOT_NAME = "linkedin_scrapy"

SPIDER_MODULES = ["linkedin_scrapy.spiders"]
NEWSPIDER_MODULE = "linkedin_scrapy.spiders"

SCRAPEOPS_API_KEY = env.str('API_KEY')
SCRAPEOPS_PROXY_ENABLED = True

DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

FEED_EXPORTERS = {
    'csv': 'linkedin_scrapy.exporters.CsvCustomSeperator'
}

FEEDS = {
    'data/%(name)s/%(name)s_%(time)s.json': {
        'format': 'json',
        'encoding': 'utf8'
    }
}