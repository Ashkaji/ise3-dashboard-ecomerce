import scrapy


class GoogleSpiderSpider(scrapy.Spider):
    name = "google_spider"
    allowed_domains = ["store.google.com"]
    start_urls = ["https://store.google.com/us/category/phones"]

    def parse(self, response):
        pass
