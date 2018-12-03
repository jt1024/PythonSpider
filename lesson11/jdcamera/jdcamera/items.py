# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdcameraItem(scrapy.Item):
    # 名称
    name = scrapy.Field()
    # 链接
    link = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 销售店铺
    owner = scrapy.Field()
    # 评论数
    comment = scrapy.Field()
