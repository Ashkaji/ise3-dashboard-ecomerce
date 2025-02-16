import scrapy


class AppleSpiderSpider(scrapy.Spider):
    name = "apple_spider"
    allowed_domains = ["www.apple.com"]
    start_urls = ["https://www.apple.com/shop/buy-iphone"]

    def parse(self, response):
        pass
