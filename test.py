import scrapy
from scrapy.crawler import CrawlerProcess
from itemadapter import ItemAdapter
import json
import datetime

class NewsItem(scrapy.Item):
    source = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    image = scrapy.Field()
    timestamp = scrapy.Field()
    url = scrapy.Field()

class GlobalNewsSpider(scrapy.Spider):
    name = 'global_news'
    allowed_domains = ['sina.com.cn', 'bbc.com']
    
    custom_settings = {
        'CONCURRENT_REQUESTS': 8,
        'DOWNLOAD_DELAY': 0.5,
        'FEED_FORMAT': 'json',
        'FEED_URI': 'news_output_%s.json' % datetime.datetime.now().strftime("%Y%m%d"),
        'ITEM_PIPELINES': {
            '__main__.JsonWriterPipeline': 300,
        }
    }

    start_urls = [
        'https://news.sina.com.cn/world/',
        'https://www.bbc.com/news'
    ]

    def parse(self, response):
        # 新浪新闻解析优化
        if 'sina' in response.url:
            for article in response.css('.news-item'):
                yield scrapy.Request(
                    url=article.css('a::attr(href)').get(),
                    callback=self.parse_sina_detail,
                    meta={
                        'source': '新浪新闻',
                        'title': article.css('a::text').get('').strip(),
                        'image': article.css('img::attr(src)').get('')
                    }
                )
        
        # BBC新闻解析优化
        elif 'bbc' in response.url:
            for article in response.css('div.gs-c-promo'):
                item = NewsItem()
                item['source'] = 'BBC News'
                item['title'] = article.css('h3::text').get('').strip()
                item['image'] = article.css('img::attr(src)').get('')
                item['timestamp'] = article.css('time::attr(datetime)').get('')
                item['url'] = response.urljoin(article.css('a::attr(href)').get(''))
                yield item

    def parse_sina_detail(self, response):
        """新浪新闻详情页解析"""
        item = NewsItem()
        item.update(response.meta)
        item['content'] = '\n'.join(response.css('.article-content p::text').getall()).strip()
        item['timestamp'] = response.css('.date::text').get('').split()[0]
        item['url'] = response.url
        yield item

class JsonWriterPipeline:
    """自定义存储管道"""
    def open_spider(self, spider):
        self.file = open(spider.settings.get('FEED_URI'), 'a', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict(), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

if __name__ == "__main__":
    process = CrawlerProcess()
    process.crawl(GlobalNewsSpider)
    process.start()