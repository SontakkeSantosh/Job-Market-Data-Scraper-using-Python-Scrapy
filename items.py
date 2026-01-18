import scrapy

class JobMarketItem(scrapy.Item):
    job_title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    skills = scrapy.Field()
    job_link = scrapy.Field()
