# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AikaNewNewItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    车型 = scrapy.Field()
    综合评分 = scrapy.Field()
    外观评分 = scrapy.Field()
    内饰评分 = scrapy.Field()
    空间评分 = scrapy.Field()
    舒适评分 = scrapy.Field()
    油耗评分 = scrapy.Field()
    动力评分 = scrapy.Field()
    操控评分 = scrapy.Field()
    性价比评分 = scrapy.Field()
    裸车价格 = scrapy.Field()
    购车地点 = scrapy.Field()
    购入时间 = scrapy.Field()
    当前油耗 = scrapy.Field()



