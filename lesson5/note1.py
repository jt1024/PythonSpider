#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/7/1 13:13
"""
import urllib.request
import http.cookiejar

# 没有伪装的爬虫请求
url = "http://news.163.com/18/0614/08/DK8DRT8F0001899N.html"
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http': "127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open(r"D:\DataguruPyhton\PythonSpider\lesson5\demo1.html", "wb")
fhandle.write(data)
fhandle.close()

# 伪装后的爬虫请求
url = "http://news.163.com/18/0614/08/DK8DRT8F0001899N.html"
# 以字典的形式设置headers
headers = {"Accept": " text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Accept-Language": " zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
           "Connection": "keep-alive",
           "referer": "http://www.163.com/"}
# 设置cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http': "127.0.0.1:8888"})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, urllib.request.HTTPCookieProcessor(cjar))
# 建立空列表，为了以指定格式存储头信息
headall = []
# 通过for循环遍历字典，构造出指定格式的headers信息
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
# 将指定格式的headers信息添加好
opener.addheaders = headall
# 将opener安装为全局
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open(r"D:\DataguruPyhton\PythonSpider\lesson5\demo2.html", "wb")
fhandle.write(data)
fhandle.close()
