import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    
    start_urls = ['http://imdb.com/']

    def parse(self, response):
        pass
