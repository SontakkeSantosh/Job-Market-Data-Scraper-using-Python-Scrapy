import csv

class JobMarketScraperPipeline:
    def open_spider(self, spider):
        self.file = open("output/jobs.csv", "w", newline="", encoding="utf-8")
        self.writer = csv.writer(self.file)
        self.writer.writerow([
            "Job Title", "Company", "Location", "Skills", "Job Link"
        ])

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow([
            item["job_title"],
            item["company"],
            item["location"],
            item["skills"],
            item["job_link"]
        ])
        return item
