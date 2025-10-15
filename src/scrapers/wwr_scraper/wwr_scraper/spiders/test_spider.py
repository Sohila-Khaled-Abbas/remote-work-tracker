import scrapy

class TestSpider(scrapy.Spider):
    name = "test"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css("span.text::text").getall()
        for q in quotes:
            yield {"quote": q}
