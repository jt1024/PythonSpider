# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CnblogPipeline(object):
    def process_item(self, item, spider):
        with open('D:/DataguruPyhton/PythonSpider/images/博客.txt', 'w', encoding='utf-8') as f:
            titles = item['title']
            links = item['link']
            for i, j in zip(titles, links):
                f.write(i + ':' + j + '\n')
        return item
