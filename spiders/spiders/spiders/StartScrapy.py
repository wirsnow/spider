from scrapy.cmdline import execute
spider = 'quotes'
execute(f'scrapy crawl {spider}'.split())