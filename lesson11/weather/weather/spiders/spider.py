# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 12:52:47 2016

@author: Administrator
"""

import scrapy
from weather.items import WeatherItem


class WeatherSpider(scrapy.Spider):
    name = "myweather"
    allowed_domains = ["sina.com.cn"]
    start_urls = ['http://weather.sina.com.cn']

    def parse(self, response):
        item = WeatherItem()
        item['city'] = response.xpath('//*[@id="slider_ct_name"]/text()').extract()
        tenDay = response.xpath('//*[@id="blk_fc_c0_scroll"]');
        item['date'] = tenDay.css('p.wt_fc_c0_i_date::text').extract()
        item['dayDesc'] = tenDay.css('img.icons0_wt::attr(title)').extract()
        item['dayTemp'] = tenDay.css('p.wt_fc_c0_i_temp::text').extract()
        return item

## 执行命令1：scrapy crawl myweather
## 执行命令2：scrapy crawl myweather -o myweather.json
