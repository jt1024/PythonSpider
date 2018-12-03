# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:53:44 2018

@author: Administrator
"""
## Selenium + PhantomJS 从百度地图中获取地址
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get('https://map.baidu.com/')
input_node = driver.find_element_by_xpath('//*[@id="sole-input"]')
input_node.send_keys('广东欧珀移动通信有限公司')
driver.find_element_by_xpath('//*[@id="search-button"]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="card-1"]/div/ul/li[1]/div[1]/div[3]/div[2]').text

driver.refresh()
input_node = driver.find_element_by_xpath('//*[@id="sole-input"]')
input_node.send_keys('广州酒家')
driver.find_element_by_xpath('//*[@id="search-button"]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="card-1"]/div/ul/li[1]/div[1]/div[3]/div[3]').text
driver.close()

## Selenium + PhantomJS 从百度拾取坐标系统中获取地址和坐标
from selenium import webdriver

driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
url = 'http://api.map.baidu.com/lbsapi/getpoint/'
driver.get(url)
company = '广东欧珀移动通信有限公司'
input_node = driver.find_element_by_xpath('//*[@id="localvalue"]')
input_node.send_keys(company)
driver.find_element_by_xpath('//*[@id="localsearch"]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="no_0"]/p').text.split('\n')
driver.close()

## 封装：Selenium + PhantomJS 从百度拾取坐标系统中获取地址和坐标
from selenium import webdriver


def get_address(company):
    input_node = driver.find_element_by_xpath('//*[@id="localvalue"]')
    input_node.send_keys(company)
    driver.find_element_by_xpath('//*[@id="localsearch"]').click()
    driver.implicitly_wait(3)
    result = driver.find_element_by_xpath('//*[@id="no_0"]/p').text.split('\n')
    return result


driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
url = 'http://api.map.baidu.com/lbsapi/getpoint/'
driver.get(url)
get_address("莱州一中")
driver.close()