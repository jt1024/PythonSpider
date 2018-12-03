#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/6/18 8:40
"""
import urllib.request
from lxml import etree

# 第1题

url = 'http://www.pythonscraping.com/pages/warandpeace.html'
with urllib.request.urlopen(url) as response:
    wb_data = response.read()

html = etree.HTML(wb_data)
res_list = html.xpath('//div[@id="text"]/span[@class="red"]/text()')
for res_item in res_list:
    print(res_item)

# 第2题

url = 'http://www.pythonscraping.com/pages/page3.html'
with urllib.request.urlopen(url) as response:
    wb_data = response.read()

html = etree.HTML(wb_data)
res_list = html.xpath('//tr[@class="gift"]')
for res_item in res_list:
    title = res_item[0].text.strip('\r\n')
    cost = res_item[2].text.strip('\r\n')
    if (-1 != title.find("Dead Parrot")):
        print("title:{0}, cost:{1}".format(title, cost))
