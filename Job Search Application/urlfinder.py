# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# import re
#
# from . import websiteurl
#
# url= websiteurl.search_websites()
#
#
# class EmailfinderSpider(CrawlSpider):
#     name = "emailfinder"
#     # allowed_domains = ["google.com"]
#
#
#     def parse_website(self, response):
#         # email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
#         # search_text = r'\b[A-Z][a-z]'
#
#         text_content = response.xpath('//text()').extract()
#         url_list = []
#         opening = "Senior React.js Developer"
#         for text in text_content:
#             emails = re.findall(opening, text)
#             if emails:
#                 url_list.append(response.url)
#                 yield {"url": url_list,
#                          "post": opening}
#
#
#     for i in url:
#
#         start_urls = [i]
#             # start_urls = ["https://www.cronj.com"]
#
#         # Rule to follow
#         rules = [
#             Rule(LinkExtractor(allow="careers"),
#                 callback="parse_website",
#                 follow=True)
#             ]

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class UrlfinderSpider(CrawlSpider):
    name = "urlfinder"
    custom_settings = {
        'FEED_FORMAT': 'jsonlines',
        'FEED_URI': 'output.json'
    }

    def __init__(self, *args, **kwargs):
        super(UrlfinderSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.pop('start_urls', [])

    def parse(self, response):
        text_content = response.xpath('//text()').extract()
        url_list = []
        opening = "Python Developer*"
        for text in text_content:
            urls = re.findall(opening, text)
            if urls:
                url_list.append(response.url)
                yield {"url": url_list, "post": opening}

        # Add more parsing logic as needed

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)
