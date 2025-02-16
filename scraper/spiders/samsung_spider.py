import scrapy


class SamsungSpiderSpider(scrapy.Spider):
    name = "samsung_spider"
    allowed_domains = ["www.samsung.com"]
    start_urls = ["https://www.samsung.com/us/mobile/phones/all-phones/"]

    def parse(self, response):
        pass
