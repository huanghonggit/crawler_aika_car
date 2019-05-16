# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import requests
from lxml import etree
from aika_new_new.items import AikaNewNewItem

item = AikaNewNewItem()
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
    res = requests.get(url).text
    html = etree.HTML(res)
    lines = html.xpath('//div[@class="home_list clearfix"]')
    return len(lines)

class AikaSpiderSpider(scrapy.Spider):
    name = 'aika_spider'
    allowed_domains = ['newcar.xcar.com.cn']
    start_urls = ['http://newcar.xcar.com.cn/']

    # 重写URL
    def start_requests(self):
        id_list = ['160','40','1468','1469','35','8','22','3865','758','164','10','1785','439','47','3814','11','2881','3099','3368','3858','1','3382','306','3897','2912','14','184','37','731','3694','384','332','3656','3010','7','99','2564','307','3014','24','3207','3187','41','3292','2456','3028','2063','3071','2731','745','1460','1236','1437','1820','391','2798','738','1452']

        for id in id_list:
            for i in range(1, 100):
                yield Request(new_url.format(page=i, id=id), callback=self.parse)
        #     page = 1
        #     while(True):
        #         yield Request(new_url.format(page=page, id=id), callback=self.parse)
        #         if lines_num(new_url) < 10:     #可以直接调用类外面的方法
        #             break
        #         else:
        #             page += 1

    def parse(self, response):
        body = unicode_body(response)
        html = etree.HTML(body)

        if html.xpath('//div[@class="home_list clearfix"]//dd/span/a/text()') is not None and len(html.xpath('//div[@class="home_list clearfix"]//dd/span/a/text()')) > 0:
            item[u"车型"] =  html.xpath('//div[@class="home_list clearfix"]//dd/span/a/@href')[0][2:-1].strip()
        # lines = html.xpath('//div[@class="home_list clearfix"]')
        # print(len(lines))
        carinfo_dict = {}
        lines = html.xpath('//div[@class="score"]')
        length = len(lines)
        try:
            if length == 0:
                print("此用户评价中无评分")
                return None
            else:
                if html.xpath('//div[@class="score"]') is not None and len(html.xpath('//div[@class="score"]')) > 0:
                    for info in lines:
                        # 提取车辆评分
                        if info.xpath('.//div[@class="score_tit"]/em/text()'):
                            item[u"综合评分"] = info.xpath('.//div[@class="score_tit"]/em/text()')[0].strip()
                        score_list = info.xpath('.//ul[@class="score_list"]/li')

                        pingfendict = {}
                        for li in score_list:
                            if  li.xpath("./em/text()") is not None and len(li.xpath("./em/text()")) > 0 and li.xpath("./span/text()") is not None and len(li.xpath("./span/text()")):
                                pingfendict[li.xpath("./span/text()")[0].strip()] = li.xpath("./em/text()")[0].strip() #把分数值赋值给dict中的值,把li里面的值存储在字典中
                            #print(pingfendict)
                            if "外观" in pingfendict.keys():
                                item[u"外观评分"] = pingfendict["外观"]
                            if "内饰" in pingfendict.keys():
                                item[u"内饰评分"] = pingfendict["内饰"]
                            if "空间" in pingfendict.keys():
                                item[u"空间评分"] = pingfendict["空间"]
                            if "舒适" in pingfendict.keys():
                                item[u"舒适评分"] = pingfendict["舒适"]
                            if "油耗" in pingfendict.keys():
                                item[u"油耗评分"] = pingfendict["油耗"]
                            if "动力" in pingfendict.keys():
                                item[u"动力评分"] = pingfendict["动力"]
                            if "操控" in pingfendict.keys():
                                item[u"操控评分"] = pingfendict["操控"]
                            if "性价比" in pingfendict.keys():
                                item[u"性价比评分"] = pingfendict["性价比"]
                        yield item
        except:
            print('提取评分失败！')


 # 提取购车信息
                # car_info = info.xpath(".//div[@class='list_infor']/dl")
                # for dl in car_info:
                #     # print(dl.xpath("./dt/text()")[0].strip())
                #     # print(dl.xpath(".//a[@target='_blank']/text()")[0].strip())
                #     # print(len(dl.xpath(".//a[@target='_blank']/text()")[0].strip()))
                #     carinfo_dict[dl.xpath("./dt/text()")[0].strip()] = dl.xpath("./dd/text()")[0].strip()
                # print(carinfo_dict)
                #item[u"裸车价格"] = info.xpath("./dl[@class='clearfix']/dd[1]/span/a/text()")[0]