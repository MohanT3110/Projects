# main.py
import logging
from . import websiteurl
from . import urlfinder
# from websiteurl import search_websites
from scrapy.crawler import CrawlerProcess
# from emailfinder import EmailfinderSpider

#configure logging
logging.basicConfig(level=logging.INFO)
logger =logging.getLogger(__name__)


# Search for website URLs
logger.info("Searching for Website urls")
website_urls = websiteurl.search_websites()
logger.info(f"Found {len(website_urls)} website URLs.")

# Run the Scrapy spider for each website URL
process = CrawlerProcess()
for url in website_urls:
    logger.info(f"Running Scrapy for URL: {url}")
    process.crawl(urlfinder.UrlfinderSpider, start_urls=[url])
logger.info("Scrapy process started.")
process.start()
logger.info("Scrapy process finished.")