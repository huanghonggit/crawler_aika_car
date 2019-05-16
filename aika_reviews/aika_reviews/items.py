# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AikaReviewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    最满意 = scrapy.Field()
    不满意 = scrapy.Field()
    外观 = scrapy.Field()
    内饰 = scrapy.Field()
    空间 = scrapy.Field()
    舒适 = scrapy.Field()
    油耗 = scrapy.Field()
    动力 = scrapy.Field()
    操控 = scrapy.Field()
    性价比 = scrapy.Field()

