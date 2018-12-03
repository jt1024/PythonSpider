#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:html_outputer.py
@time:2018/7/17 7:59
"""
import os


class HtmlOutputer(object):
    def output_html(self, data):
        if data is None:
            return

        parent_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(parent_dir, 'htmldir')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        name = data['title'] + '.html'
        imglocalpath = os.path.join(output_dir, name)
        fout = open(imglocalpath, 'w', encoding='utf-8')

        fout.write("<html>")
        fout.write("<body>")
        fout.write("<div _class='url'>%s</div>" % data['url'])
        fout.write("<div _class=title>%s</div>" % data['title'])
        fout.write('<div _class="content">')
        for i in range(len(data['content'])):
            fout.write("<div>%s</div>" % data['content'][i])
        fout.write("</div>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
