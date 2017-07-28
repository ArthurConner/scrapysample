# -*- coding: utf-8 -*-
import scrapy
from life.items import LifeItem
from scrapy.http import Request
from scrapy.loader import ItemLoader

class BasicSpider(scrapy.Spider):
	name = 'manual'
	allowed_domains = ['web','lifeinrestandmotion.blogspot.com']
	start_urls = ['http://lifeinrestandmotion.blogspot.com']

	def parse_item(self, response):
		l = ItemLoader(item=LifeItem(), response=response)
		#item = LifeItem()
		l.add_value('url', response.url)
		l.add_xpath('piece_urls','//div[@class="post-body entry-content"]/div/text()')
		#.extract()
		#self.log("got items")
		return l.load_item()

	def parse(self, response):
		next_selector = response.xpath('//*[@id="Blog1"]/div/div/div/div/div/h3//@href').extract()
		for url in next_selector:
			#self.log("go to url %s",str(url))
			yield Request(url,callback=self.parse_item)
