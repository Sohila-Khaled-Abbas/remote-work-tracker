import scrapy

class JobItem(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    category = scrapy.Field()
    tags = scrapy.Field()
    date_posted = scrapy.Field()
    salary = scrapy.Field()
    region = scrapy.Field()
    job_link = scrapy.Field()
    description = scrapy.Field()
