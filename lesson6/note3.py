#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/7/9 0:05
"""

'''
采集数据前的思考：
1、需要采集什么数据
2、url队列的优先方法
3、有没有不想抓取的网站
4、如何避免法律上的责任
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
allExtLinks = set()
allIntLinks = set()


# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/.*" + includeUrl + ")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not in internalLinks:
                internalLinks.append(link.attrs["href"])
    return internalLinks


# 获取所有外链的列表
def getExternallLinks(bsObj, excludeUrl):
    externalLinks = []
    # Finds all links that start with "http" or "www" that do not contain the current URL
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!" + excludeUrl + ").)*$")):
        if link.attrs["href"] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


# url拆分
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts


# Collects a list of all external URLs found on the site
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    internalLinks = getInternalLinks(bsObj, splitAddress(siteUrl)[0])
    externalLinks = getExternallLinks(bsObj, splitAddress(siteUrl)[0])

    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.add(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.add(link)
            getAllExternalLinks("http:" + link)


getAllExternalLinks("http://oreilly.com")


# pages = set()
# def getRandomExternalLink(startingPage):
#     html = urlopen(startingPage)
#     bsObj = BeautifulSoup(html, 'lxml')
#     getExternalLinks = getExternallLinks(bsObj, splitAddress(startingPage)[0])
#     if len(getExternalLinks) == 0:
#         internalLinks = getExternallLinks(startingPage)
#         return internalLinks[random.randint(0, len(internalLinks) - 1)]
#     else:
#         return getExternalLinks[random.randint(0, len(getExternalLinks) - 1)]
#
#
# def followExternalOnly(startingSite):
#     externalLink = getRandomExternalLink(startingSite)
#     print("Random external link is: " + externalLink)
#     followExternalOnly(externalLink)
#
#
# followExternalOnly("http://oreilly.com")
