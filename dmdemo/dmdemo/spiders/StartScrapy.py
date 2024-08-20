from scrapy.cmdline import execute
spider = 'httpbin'
execute(f'scrapy crawl {spider}'.split())