BOT_NAME = "job_market_scraper"

SPIDER_MODULES = ["job_market_scraper.spiders"]
NEWSPIDER_MODULE = "job_market_scraper.spiders"

ROBOTSTXT_OBEY = True
DOWNLOAD_DELAY = 2

ITEM_PIPELINES = {
    "job_market_scraper.pipelines.JobMarketScraperPipeline": 300,
}

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
