# -*- coding: utf-8 -*-
import scrapy
from life.items import LifeItem

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['web']
    start_urls = ['http://lifeinrestandmotion.blogspot.com']

    def parse(self, response):
    	item = LifeItem()
    	item['piece_urls'] =  response.xpath('//*[@id="Blog1"]/div/div/div/div/div/h3//@href').extract()
    	return item
