import scrapy
from job_market_scraper.items import JobMarketItem

class JobsSpider(scrapy.Spider):
    name = "jobs"
    allowed_domains = ["example.com"]
    start_urls = [
        "https://example.com/jobs"
    ]

    def parse(self, response):
        jobs = response.css("div.job-card")

        for job in jobs:
            item = JobMarketItem()
            item["job_title"] = job.css("h2::text").get()
            item["company"] = job.css("span.company::text").get()
            item["location"] = job.css("span.location::text").get()
            item["skills"] = ", ".join(job.css("span.skill::text").getall())
            item["job_link"] = response.urljoin(
                job.css("a::attr(href)").get()
            )
            yield item
