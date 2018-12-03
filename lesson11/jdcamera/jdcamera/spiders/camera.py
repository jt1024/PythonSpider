#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:camera.py
@time:2018/8/19 23:58
"""

import scrapy
from jdcamera.items import JdcameraItem
from scrapy.http import Request
import re
from scrapy_splash import SplashRequest


class CameraSpider(scrapy.Spider):
    name = "jdcamera"
    allowed_domains = ["list.jd.com"]
    start_urls = (
        'https://list.jd.com/list.html?cat=652,654,831',
        # "https://list.jd.com/list.html?cat=652,654,831&page=1&sort=sort_totalsales15_desc&trans=1&JL=6_0_0#J_main"
    )

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse,
                                args={'wait': 1}, endpoint='render.html')

    def parse(self, response):
        for sel in response.xpath('//*[@id="plist"]/ul/li/div[@class="gl-i-wrap j-sku-item"]'):
            item = JdcameraItem()
            # 链接
            item["link"] = "http:" + str(sel.xpath('div[1]/a/@href').extract())[2:-2]
            # 价格
            item["price"] = sel.xpath('div[2]/strong[1]/i/text()').extract()
            # 商品名称
            temp = str(sel.xpath('div[3]/a/em/text()').extract())
            pattern = re.compile("[\u4e00-\u9fa5]+.+\w")  # 从第一个汉字起 匹配商品名称
            good_name = re.search(pattern, temp)
            item["name"] = good_name.group()
            # 评论数
            item["comment"] = sel.xpath('div[4]/strong/a/text()').extract()
            # 销售店铺
            item["owner"] = sel.xpath('div[5]/span/a/text()').extract()
            # 提取完后返回item
            yield item

        # 通过循环自动爬取127页的数据
        for i in range(2, 128):
            # 通过上面总结的网址格式构造要爬取的网址
            url = "https://list.jd.com/list.html?cat=652,654,831&page=" + str(i) + "&sort=sort_totalsales15_desc&trans=1&JL=6_0_0"
            # 通过yield返回Request，并指定要爬取的网址和回调函数
            # 实现自动爬取
            # yield Request(url, callback=self.parse)
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 1}, endpoint='render.html')
