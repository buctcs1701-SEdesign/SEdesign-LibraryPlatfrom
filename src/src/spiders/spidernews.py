# -*- coding: utf-8 -*-
import scrapy


class SpidernewsSpider(scrapy.Spider):
    name = 'spidernews'
    allowed_domains = ['spidernews.com']
    start_urls = ['http://spidernews.com/']

    def parse(self, response):
        pass
