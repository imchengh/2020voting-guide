from os import remove

from scrapy.crawler import CrawlerProcess

from spider import LawSpider

OUTPUT_RAW = "../data/raw/law.json"


def remove_output():
    try:
        remove(OUTPUT_RAW)
    except FileNotFoundError:
        print(f"File not exist: {OUTPUT_RAW}")


def scrapy_crawl():
    process = CrawlerProcess(
        {
            "USER_AGENT": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
            "FEED_FORMAT": "json",
            "FEED_EXPORT_ENCODING": "utf-8",
            "FEED_URI": OUTPUT_RAW,
            "CONCURRENT_REQUESTS": 1,
            "DOWNLOAD_DELAY": 1,
        }
    )
    process.crawl(LawSpider)
    process.start()


if __name__ == "__main__":
    remove_output()
    scrapy_crawl()
