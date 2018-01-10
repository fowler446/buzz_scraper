# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class BuzzScraperItem(scrapy.Item):
    post_title = scrapy.Field()
    post_items = scrapy.Field()
