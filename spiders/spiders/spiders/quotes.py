import scrapy
from ..items import QuoteItem


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response,*args, **kwargs):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            item = QuoteItem()
            item['quote'] = quote.xpath('.//span[@class="text"]/text()').extract_first()
            item['author'] = quote.xpath('.//small[@class="author"]/text()').extract_first()
            item['tags'] = quote.xpath('.//div[@class="tags"]/a/text()').extract()
            yield item
        next = response.xpath('//li[@class="next"]/a/@href').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url, callback=self.parse)