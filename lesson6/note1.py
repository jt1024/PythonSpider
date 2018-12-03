#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/7/8 23:35
"""
'''获取网页https://en.wikipedia.org/wiki/Kevin_Bacon中的词条url链接'''

## 尝试1：爬取网页内容
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(r'https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'lxml')
print(bsObj.prettify())

## 尝试2:抓取网页中的 a 标签，且以 href 开头的所有url链接
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen(r'https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'lxml')
allLinks = bsObj.findAll("a")
print(len(allLinks))  # 780
for link in allLinks:
    if "href" in link.attrs:
        print(link.attrs["href"])

## 分析“尝试2”中的数据后发现如下规律：1、id在bodyContent的div标签中；2、url不包含冒号；3、url以/wiki/开头
## 正式提取维基中的词条url
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen(r'https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'lxml')
allLinks = bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))
# allLinks
# allLinks[0]
# # result: <a class="mw-disambig" href="/wiki/Kevin_Bacon_(disambiguation)" title="Kevin Bacon (disambiguation)">Kevin Bacon (disambiguation)</a>
# allLinks[0].text
# # result: 'Kevin Bacon (disambiguation)'
# allLinks[0].attrs['class']
# # result: ['mw-disambig']
# allLinks[0].attrs['href']
# # result: '/wiki/Kevin_Bacon_(disambiguation)'
# allLinks[0].attrs['title']
# # result: 'Kevin Bacon (disambiguation)'
# print(len(allLinks))  # 380
for link in allLinks:
    if 'href' in link.attrs:
        print(link.attrs['href'])

# 知识点：正则表达式之 pattern+?、pattern*?、(?!pattern)、(?:pattern)
# pattern+?、pattern*?
# 这两个比较常用，表示懒惰匹配，即匹配符合条件的尽量短的字符串。默认情况下 + 和 * 是贪婪匹配，即匹配尽可能长的字符串，在它们后面加上 ? 表示想要进行懒惰匹配。
# (?!pattern)
# 表示一个过滤条件，若字符串符合 pattern 则将其过滤掉。在分析日志时很有用，例如想过滤掉包含 info 标记的日志可以写 ^(?!.*info).*$。
# (?:pattern)
# 这条规则主要是为了优化性能，对匹配没有影响。它表示括号内的子表达式匹配的结果不需要返回也不会被 $1 $2 之类的反向引用。



'''延伸：获取网页https://en.wikipedia.org/wiki/Kevin_Bacon中的词条url链接以及关联页面中的词条url'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random


def getLinks(articleUrl):
    html = urlopen("https://en.wikipedia.org" + articleUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find('div', {'id': 'bodyContent'}).findAll('a', href=re.compile("^(/wiki/)((?!:).)*$"))


links = getLinks("/wiki/Kevin_Bacon")
random.seed(datetime.datetime.now())  # 设置随机因子为系统时间，这样再使用随机函数时就不会取到重复值了
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)
# 上述代码存在两个隐患：隐患1，有可能会从A页面到B页面再到A页面；隐患2，没有做异常处理
