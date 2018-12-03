#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:csdn_spider.py
@time:2018/8/13 22:04
"""

import scrapy
from tutorial.items import CsdnItem


class CsdnSpider(scrapy.Spider):
    name = "csdn"
    allowed_domains = ["csdn.net"]
    start_urls = [
        "https://blog.csdn.net/jiangwei0910410003/article/details/79436956",
        "https://blog.csdn.net/M7720EIoSi6oA9/article/details/81463841"
    ]

    def parse(self, response):
        ## 入门1
        # filename = "D:/DataguruPyhton/PythonSpider/images/" + response.url.split("/")[-1] + ".txt"
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        ## 入门2
        # for sel in response.xpath('//*[@id="asideProfile"]'):
        #     author = sel.xpath('div[1]/div[2]/p[1]/a/text()').extract()
        #     fans = sel.xpath('div[2]/dl[2]/dd/span/text()').extract()
        #     like = sel.xpath('div[2]/dl[3]/dd/span/text()').extract()
        #     comment = sel.xpath('div[2]/dl[4]/dd/span/text()').extract()
        #     print(author, fans, like, comment)

        ## 入门3
        for sel in response.xpath('//*[@id="asideProfile"]'):
            item = CsdnItem()
            item['author'] = sel.xpath('div[1]/div[2]/p[1]/a/text()').extract()
            item['fans'] = sel.xpath('div[2]/dl[2]/dd/span/text()').extract()
            item['like'] = sel.xpath('div[2]/dl[3]/dd/span/text()').extract()
            item['comment'] = sel.xpath('div[2]/dl[4]/dd/span/text()').extract()
            yield item
