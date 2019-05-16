# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import requests
from lxml import etree
from aika_reviews.items import AikaReviewsItem

item = AikaReviewsItem()
new_url = 'http://newcar.xcar.com.cn/auto/index.php?r=reputation/reputation/GetAjaxKbList3&page={page}&pserid={id}&jh=0&wd=0'

# 正确编码问题
# python3中的str 对应python2中的unicode, 所以python3中没有unicode
def unicode_body(response):
    if isinstance(response.body, str):
        return response.body
    try:
        return response.body_as_unicode()
    except:
        try:
            return response.body.decode(response.encoding)
        except:
            raise Exception("Cannot convert response body to unicode!")

# 提取每一页的评论数
def lines_num(url):
    #print(url)
    res = requests.get(url).text
    html = etree.HTML(res)
    lines = html.xpath('//div[@class="home_list clearfix"]')
    # print(type(lines))
    # print(len(lines))
    return len(lines)

class AikaSpiderSpider(scrapy.Spider):
    name = 'aika_spider'
    allowed_domains = ['newcar.xcar.com.cn']
    start_urls = ['http://newcar.xcar.com.cn/']

    def start_requests(self):
        id_list =['258', '1217', '1406', '2516']#, , ]
        for id in id_list:
            # for i in range(1, 200):
            #     yield Request(new_url.format(page=i, id=id), callback=self.parse)
            page = 1
            while(True):
                url = new_url.format(page=page, id=id)
                yield Request(url=url, callback=self.parse)
                if lines_num(url) < 10:     #可以直接调用类外面的方法
                    break
                else:
                    page +=1

    def parse(self, response):
        body = unicode_body(response)
        html = etree.HTML(body)
        lines = html.xpath('//div[@class="home_list clearfix"]')
        print(len(lines))
        for info in lines:
            if info.xpath('.//dl[@class="dw_22"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_22"]/dd/text()')) > 0:
                item[u"最满意"] = info.xpath('.//dl[@class="dw_22"]/dd/text()')
            if info.xpath('.//dl[@class="dw_23"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_23"]/dd/text()')) > 0:
                item[u"不满意"] = info.xpath('.//dl[@class="dw_23"]/dd/text()')
            if info.xpath('.//dl[@class="dw_1"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_1"]/dd/text()')) > 0:
                item[u"外观"] = info.xpath('.//dl[@class="dw_1"]/dd/text()')
            if info.xpath('.//dl[@class="dw_2"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_2"]/dd/text()')) > 0:
                item[u"内饰"] = info.xpath('.//dl[@class="dw_2"]/dd/text()')
            if info.xpath('.//dl[@class="dw_3"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_3"]/dd/text()')) > 0:
                item[u"空间"] = info.xpath('.//dl[@class="dw_3"]/dd/text()')
            if info.xpath('.//dl[@class="dw_4"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_4"]/dd/text()')) > 0:
                item[u"舒适"] = info.xpath('.//dl[@class="dw_4"]/dd/text()')
            if info.xpath('.//dl[@class="dw_5"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_5"]/dd/text()')) > 0:
                item[u"油耗"] = info.xpath('.//dl[@class="dw_5"]/dd/text()')
            if info.xpath('.//dl[@class="dw_6"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_6"]/dd/text()')) > 0:
                item[u"动力"] = info.xpath('.//dl[@class="dw_6"]/dd/text()')
            if info.xpath('.//dl[@class="dw_7"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_7"]/dd/text()')) > 0:
                item[u"操控"] = info.xpath('.//dl[@class="dw_7"]/dd/text()')
            if info.xpath('.//dl[@class="dw_8"]/dd/text()') is not None and len(info.xpath('.//dl[@class="dw_8"]/dd/text()')) > 0:
                item[u"性价比"] = info.xpath('.//dl[@class="dw_8"]/dd/text()')
            yield item