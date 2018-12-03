#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/8/10 8:58
"""

## 快速体验Selenium： 打开浏览器，并自动访问百度首页
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')

## 快速体验Selenium： 打开浏览器，并自动在百度中搜索“Python”关键词
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')
input.send_keys('Python')
input.send_keys(Keys.ENTER)

## 【爬取代码】快速体验Selenium： 打开浏览器，并自动在百度中搜索“Python”关键词
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()

##
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print(driver.page_source)

# from selenium import webdriver
#
# # 我们首先导入了Selenium里的webdriver，
# browser = webdriver.PhantomJS()
# # 然后建立一个PhantomJS的浏览器对象，
# url = 'https://www.baidu.com'
# browser.get(url)
# # 最后我们通过get方法，打开了百度的首页。
# browser.implicitly_wait(3)
#
#
# https://www.cnblogs.com/freeman818/p/7352040.html
# https://blog.csdn.net/qq_30242609/article/details/70859891
#
# UserWarning: Selenium support for PhantomJS has been deprecated, please use headless versions of Chrome or Firefox instead
#   warnings.warn('Selenium support for PhantomJS has been deprecated, please use headless '
#
# https://blog.csdn.net/qq_30242609/article/details/79323963

from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r'E:\JIAT\BOOK\炼数成金\python网络爬虫应用实战\7.Selenium与模拟浏览器-PhantomJS\代码\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# driver.page_source
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()
