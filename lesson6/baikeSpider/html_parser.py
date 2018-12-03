#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:html_parser.py
@time:2018/7/17 7:59
"""
from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/item/.+"))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        res_data = {}
        # url
        res_data['url'] = page_url
        # <dd class="lemmaWgt-lemmaTitle-title">
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find('h1')
        res_data['title'] = title_node.get_text()
        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()
        # <div class="para" label-module="para">Python的创始人为Guido van Rossum。1989年圣诞节期间，在<a target="_blank" href="/item/%E9%98%BF%E5%A7%86%E6%96%AF%E7%89%B9%E4%B8%B9/2259975" data-lemmaid="2259975">阿姆斯特丹</a>，Guido为了打发<a target="_blank" href="/item/%E5%9C%A3%E8%AF%9E%E8%8A%82/127881" data-lemmaid="127881">圣诞节</a>的无趣，决心开发一个新的脚本解释程序，作为ABC 语言的一种继承。之所以选中Python（大蟒蛇的意思）作为该编程语言的名字，是因为他是一个叫Monty Python的喜剧团体的<a target="_blank" href="/item/%E7%88%B1%E5%A5%BD%E8%80%85">爱好者</a>。</div>
        content_node = soup.findAll('div', class_='para')
        n = len(content_node)
        content = {}
        for i in range(n):
            content[i] = content_node[i].get_text()
        res_data['content'] = content
        return res_data

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
