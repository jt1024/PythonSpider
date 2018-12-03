#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/7/1 14:31
"""

import mechanicalsoup  # 加载扩展包

browser = mechanicalsoup.StatefulBrowser()  # 创建一个浏览器对象
browser.open("https://accounts.douban.com/login")  # 打开网页

# print(browser.get_url())  # 查看浏览器当前的网站
# print(browser.get_current_page())  # 获取当前网页的内容

browser.select_form('#lzform')  # 从当前网页中选择一个表单，参数为CSS选择器
# 填写表单内容
browser["form_email"] = "524sjl@163.com"
browser["form_password"] = "cr163yizhong."

# 使用本地浏览器打开当前页面
# browser.launch_browser()

# 展示表单的内容
browser.get_current_form().print_summary()

# 提交表单
response = browser.submit_selected()
# 获取提交后的网页信息
print(response.text)
