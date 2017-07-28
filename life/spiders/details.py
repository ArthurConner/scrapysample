# -*- coding: utf-8 -*-
import scrapy
from life.items import LifeItem
from scrapy.http import Request
from scrapy.loader import ItemLoader

class BasicSpider(scrapy.Spider):
	name = 'details'
	allowed_domains = ['web','lifeinrestandmotion.blogspot.com']
	start_urls = ['http://lifeinrestandmotion.blogspot.com']

	def parse_item(self, response):
		l = ItemLoader(item=LifeItem(), response=response)
		l.add_value('url', response.url)
		inner =  response.xpath('//div[@class="post-body entry-content"]/div/text()').extract()
		
		if len(inner) < 1:
			inner =  response.xpath('//div[@class="post-body entry-content"]/p/text()').extract()
			
		if len(inner) < 1:
			inner =  response.xpath('//div[@class="post-body entry-content"]/text()').extract()
		
		l.add_value('piece_paragraphs',inner)
		
		depth = 0
		if "depth" in response.meta:
			depth =  response.meta["depth"]
		
		l.add_value('depth',depth)
		
		l.add_xpath('piece_date','//h2[@class = "date-header"]/span/text()')
		l.add_xpath('title','//h3[@class = "post-title entry-title"]/text()')
		
		yield l.load_item()
		
		next_selector = response.xpath('//a[@class="blog-pager-older-link"]//@href').extract()
		for url in next_selector:
			yield Request(url,callback=self.parse_item, meta={"depth":depth + 1})

		return l.load_item()

	def parse(self, response):
		next_selector = response.xpath('//*[@id="Blog1"]/div/div/div/div/div/h3//@href').extract()
		for url in next_selector:
			#self.log("go to url %s",str(url))
			yield Request(url,callback=self.parse_item, meta={"depth":0})
