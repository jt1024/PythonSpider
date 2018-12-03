#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/7/9 0:05
"""

'''获取词条以及关联词条的url、标题、概要'''
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()  # url容器，作用：收集新的url链接；剔除已抓取的url


def getLinks(pageUrl):
    global pages  # 设为全局变量
    html = urlopen("https://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "lxml")
    try:
        # 维基词条页面的特征：
        # 1、所有的标题都在h1->span标签里，而且只有一个标题标签
        # 2、正文文字在div#bodyContent标签里；第一段文字 div#mw-content-text->p
        # 3、编辑链接只出现在词条页面上，位于li#ca-edit标签里的 li#caedit->span->a
        print("https://en.wikipedia.org" + pageUrl)
        print(bsObj.h1.get_text())
        print(bsObj.find(id="mw-content-text").findAll("p")[0])
        print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    except AttributeError:
        print("This page is missing something! No worries though!")

    allLinks = bsObj.find_all("a", href=re.compile("^(/wiki/)((?!:).)*$"))
    for link in allLinks:
        if 'href' in link.attrs:
            newPage = link.attrs['href']
            print("------------------------\n" + newPage)
            pages.add(newPage)
            getLinks(newPage)


getLinks("/wiki/Farouk_Topan")
