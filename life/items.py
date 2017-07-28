# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LifeItem(scrapy.Item):
	# define the fields for your item here like:
	piece_paragraphs = scrapy.Field()
	url = scrapy.Field()
	piece_date = scrapy.Field()
	date = scrapy.Field()
	title = scrapy.Field()
	depth = scrapy.Field()
	#date = scrapy.Field()
	#pass
