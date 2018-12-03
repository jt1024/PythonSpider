#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/8/12 18:08
"""
"""爬取京东的商品评论(通过打开界面浏览器)"""
from selenium import webdriver
from urllib.parse import quote

driver = webdriver.Chrome()  # 打开浏览器
key = '红酒'  # 设置搜索商品关键词
url = 'https://search.jd.com/Search?keyword=' + quote(key) + '&enc=utf-8'  # 构造url
driver.get(url)  # 打开url
driver.implicitly_wait(3)  # 等待
links = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a')  # 查找当前页面的商品链接
urls = [l.get_attribute('href') for l in links]
url = urls[1]  # 获取第一个商品链接
driver.get(url)  # 打开页面
driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()  # 点击商品评论
# 获取评论数据
comment_list = driver.find_elements_by_xpath('//*[@id="comment-0"]//div/div[2]/p')
comment_text_list = [c.text for c in comment_list]
driver.find_element_by_link_text('下一页').click()  # 点击下一页评论
driver.close()

"""爬取京东的商品评论(通过无界面浏览器)"""
from selenium import webdriver
from urllib.parse import quote

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
key = '红酒'  # 设置搜索商品关键词
url = 'https://search.jd.com/Search?keyword=' + quote(key) + '&enc=utf-8'  # 构造url
driver.get(url)  # 打开url
driver.implicitly_wait(3)  # 等待
links = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[3]/a')  # 查找当前页面的商品链接
urls = [l.get_attribute('href') for l in links]
url = urls[1]  # 获取第一个商品链接
driver.get(url)  # 打开页面
driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()  # 点击商品评论
# 获取评论数据
comment_list = driver.find_elements_by_xpath('//*[@id="comment-0"]//div/div[2]/p')
comment_text_list = [c.text for c in comment_list]
# driver.find_element_by_link_text('下一页').click()  # TODO 报错：Message: no such element: Unable to locate element: {"method":"link text","selector":"下一页"}

# import pandas as pd
# comment = pd.DataFrame(comment_text_list)
# comment.to_csv('D:/DataguruPyhton/PythonSpider/images/ptj.csv')