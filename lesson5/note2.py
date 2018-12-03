#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/7/1 14:21
"""

import mechanicalsoup  # 加载扩展包

browser = mechanicalsoup.StatefulBrowser()  # 创建一个浏览器对象
browser.open("http://httpbin.org/")  # 打开网页

print(browser.get_url())  # 查看浏览器当前的网站
browser.follow_link("forms")  # 追加url
print(browser.get_url())  # 查看当前url
print(browser.get_current_page())  # 获取当前网页的内容

browser.select_form('form[action="/post"]')  # 从当前网页中选择一个表单，参数为CSS选择器
# 填写表单内容
browser["custname"] = "Me"
browser["custtel"] = "00 00 0001"
browser["custemail"] = "nobody@example.com"
browser["size"] = "medium"
browser["topping"] = "onion"
browser["topping"] = ("bacon", "cheese")
browser["comments"] = "This pizza looks really good :-)"

# 使用本地浏览器打开当前页面
browser.launch_browser()

# 展示表单的内容
browser.get_current_form().print_summary()

# 提交表单
response = browser.submit_selected()
# 获取提交后的网页信息
print(response.text)
