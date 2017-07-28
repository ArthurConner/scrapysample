# -*- coding: utf-8 -*-
import scrapy
from life.items import LifeItem

class BasicSpider(scrapy.Spider):
    name = 'text'
    allowed_domains = ['web']
    start_urls = ['http://lifeinrestandmotion.blogspot.com/2015/08/e-e.html']

    def parse(self, response):
    	item = LifeItem()
    	item['piece_urls'] =  response.xpath('//div[@class="post-body entry-content"]/div/text()').extract()
    	return item
