# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ChongqingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    index=scrapy.Field()
    title=scrapy.Field()
    question=scrapy.Field()
    answer=scrapy.Field()
    flag=scrapy.Field()

