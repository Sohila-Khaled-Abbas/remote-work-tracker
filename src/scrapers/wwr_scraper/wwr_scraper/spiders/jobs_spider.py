import scrapy
from ..items import JobItem

class WeWorkRemotelySpider(scrapy.Spider):
    name = "weworkremotely"   # ← must match your command exactly
    allowed_domains = ["weworkremotely.com"]
    start_urls = ["https://weworkremotely.com/remote-jobs/search?term=data"]

    def parse(self, response):
        jobs = response.css('section.jobs li a:not(.view-all)')
        for job in jobs:
            link = response.urljoin(job.attrib['href'])
            yield scrapy.Request(link, callback=self.parse_job)

        # Pagination
        next_page = response.css('a.next_page::attr(href)').get()
        if next_page:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_job(self, response):
        item = JobItem()
        item['job_title'] = response.css('h1::text').get()
        item['company'] = response.css('div.listing-header-container > h2::text').get()
        item['category'] = response.css('div.listing-header-container > h3::text').get()
        item['tags'] = response.css('span.listing-tag::text').getall()
        item['date_posted'] = response.css('time::attr(datetime)').get()
        item['region'] = response.css('div.location::text').get()
        item['salary'] = response.css('span.salary::text').get()
        item['description'] = " ".join(response.css('div.listing-container p::text').getall())
        item['job_link'] = response.url
        yield item
