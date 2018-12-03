#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note3.py
@time:2018/8/12 10:21
"""
## 快速体验
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com/')
print('打开浏览器')
print(driver.title)
driver.find_element_by_id('kw').send_keys('测试')
print('关闭')
driver.quit()
print('测试完成')

## Selenium + Headless Chrome 实例一
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1366, 768)
# get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)
driver.get("http://www.baidu.com/")
# 获取页面名为wraper的id标签的文本内容
data = driver.find_element_by_id('wrapper').text
# 打印数据内容
print(data)
# 把百度设为主页关于百度About  Baidu百度推广
# ©2018 Baidu 使用百度前必读 意见反馈 京ICP证030173号  京公网安备11000002000001号
print(driver.title)  # result: 百度一下，你就知道
# 生成页面快照并保存
driver.save_screenshot(r'D:\DataguruPyhton\PythonSpider\images\baidu.png')
# id="kw"是百度搜索输入框，输入字符串"长城"
driver.find_element_by_id('kw').send_keys(u'长城')
# id="su"是百度搜索按钮，click()是模拟点击
driver.find_element_by_id('su').click()
# 获取新的页面快照
driver.save_screenshot(r'D:\DataguruPyhton\PythonSpider\images\长城.png')
# 打印网页渲染后的源代码
print(driver.page_source)
# 获取当前页面Cookie
print(driver.get_cookies())
driver.quit()

## Selenium + Headless Chrome 实例二
from selenium import webdriver
import time
# 调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.set_window_size(1366, 768)
# get方法会一直等到页面加载，然后才会继续程序，通常测试会在这里选择time.sleep(2)
driver.get("http://www.baidu.com/")
# id="kw"是百度搜索输入框，输入字符串"情人节"
driver.find_element_by_id('kw').send_keys(u'情人节')
# ctrl+a全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# ctrl+x剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
# 输入框重新输入内容
driver.find_element_by_id('kw').send_keys('鲜花')
# 模拟Enter回车键
driver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
# 清空输入框内容
driver.find_element_by_id('kw').clear()
# 生成新的页面快照
driver.save_screenshot(r'D:\DataguruPyhton\PythonSpider\images\鲜花.png')
# 获取当前url
print(driver.current_url)
driver.quit()

## Selenium + Headless Chrome 实例三：爬取包含Ajax的动态网页数据：通过手动延时
from selenium import webdriver
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
# driver.page_source
time.sleep(3)
print(driver.find_element_by_id("content").text)
driver.close()

## 【完善后的代码】爬取包含Ajax的动态网页数据：通过检查页面是否加载完毕
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()

## Selenium + Headless Chrome 实例四：爬取重定向的动态网页数据
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
import time


def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)



# from selenium import webdriver
#
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.baidu.com')
# print(driver.title)
# driver.get_screenshot_as_file(r'D:\DataguruPyhton\PythonSpider\images\baidu1.png')
# driver.close()
#
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.baidu.com')
# print(driver.title)
# driver.get_screenshot_as_file(r'D:\DataguruPyhton\PythonSpider\images\baidu2.png')
# driver.close()
#
