import scrapy

class WeWorkRemotelySpider(scrapy.Spider):
    name = "weworkremotely"
    start_urls = ["https://weworkremotely.com/remote-jobs/search?term=data"]

    def parse(self, response):
        jobs = response.css('section.jobs li a:not(.view-all)')
        for job in jobs:
            title = job.css('span.title::text').get()
            company = job.css('span.company::text').get()
            link = response.urljoin(job.attrib['href'])
            yield {
                "job_title": title,
                "company": company,
                "job_link": link
            }
