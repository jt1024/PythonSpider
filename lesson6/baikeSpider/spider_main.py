#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:spider_main.py
@time:2018/7/17 8:00
"""

import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print('craw %d:%s' % (count, new_url))
            except:
                print(1)
            try:
                html_content = self.downloader.download(new_url)
            except:
                print(2)
            try:
                new_urls, new_data = self.parser.parse(new_url, html_content)
            except:
                print(3)
            try:
                self.urls.add_new_urls(new_urls)
            except:
                print(4)
            try:
                self.outputer.output_html(new_data)
            except:
                print(5)

            count = count + 1
            if count == 5:
                break


if __name__ == "__main__":
    root_url = "https://baike.baidu.com/item/Python/407313"
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)
