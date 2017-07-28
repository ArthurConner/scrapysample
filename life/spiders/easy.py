# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from life.items import LifeItem
from scrapy.http import Request
from scrapy.loader import ItemLoader

class EasySpider(CrawlSpider):
	name = 'easy'
	allowed_domains = ['web','lifeinrestandmotion.blogspot.com']
	start_urls = ['http://lifeinrestandmotion.blogspot.com']

	rules = (
		Rule(LinkExtractor(restrict_xpaths='//*[@id="Blog1"]/div/div/div/div/div/h3'),callback='parse_item'),
	)

	def parse_item(self, response):
		l = ItemLoader(item=LifeItem(), response=response)
		l.add_value('url', response.url)
		l.add_xpath('piece_urls','//div[@class="post-body entry-content"]/div/text()')
		#self.log("got items")
		return l.load_item()
