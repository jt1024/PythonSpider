#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/8/11 20:01
"""

## selenium + phantomJs 实例一
from selenium import webdriver
# 调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用指定的PhantomJS浏览器创建浏览器对象（没有在环境变量中指定PhantomJS位置）
driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象（如果已经在环境变量中指定了PhantomJS位置）
# driver = webdriver.PhantomJS()
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

## selenium + phantomJs 实例二
from selenium import webdriver
import time
# 调用键盘按键操作需要引入keys包
from selenium.webdriver.common.keys import Keys

# 调用指定的PhantomJS浏览器创建浏览器对象（没有在环境变量中指定PhantomJS位置）
driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象（如果已经在环境变量中指定了PhantomJS位置）
# driver = webdriver.PhantomJS()
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

## Selenium + PhantomJS 实例三：爬取包含Ajax的动态网页数据：通过手动延时
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
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
import time

driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
try:
    element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "loadedButton")))
finally:
    print(driver.find_element_by_id("content").text)
    driver.close()

## Selenium + PhantomJS 实例五：爬取重定向的动态网页数据
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


driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
driver.get("http://pythonscraping.com/pages/javascript/redirectDemo1.html")
waitForLoad(driver)
print(driver.page_source)

## 彩蛋：Pillow 图象处理，为抓取验证码做知识储备
# 需要先安装pillow,安装方法：pip install pillow
from PIL import Image, ImageFilter

kitten = Image.open(u"D:\DataguruPyhton\PythonSpider\images\girl1.jpg")
blurryKitten = kitten.filter(ImageFilter.GaussianBlur)
blurryKitten.save(u"D:\DataguruPyhton\PythonSpider\images\girl2.jpg")
blurryKitten.show()









#
# # 规范文字读取
# from PIL import Image
# import subprocess
#
#
# def cleanFile(filePath, newFilePath):
#     image = Image.open(filePath)
#
#     # Set a threshold value for the image, and save
#     image = image.point(lambda x: 0 if x < 143 else 255)
#     image.save(newFilePath)
#
#     # call tesseract to do OCR on the newly created image
#     subprocess.call(["tesseract", newFilePath, "output"])
#
#     # Open and read the resulting data file
#     outputFile = open("output.txt", 'r')
#     print(outputFile.read())
#     outputFile.close()
#
#
# cleanFile("D:/Program Files (x86)/Tesseract-OCR/pic2.tif",
#           "D:/Program Files (x86)/Tesseract-OCR/pic3.png")
#
# # 从网站中抓取文字
# import time
# from urllib.request import urlretrieve
# from selenium import webdriver
#
# driver = webdriver.PhantomJS(executable_path=r'D:\python\PythonLibs\phantomjs-2.1.1-windows\bin\phantomjs')
# # driver = webdriver.Firefox(executable_path=u'C:/Program Files (x86)/Mozilla Firefox/firefox')
# driver.get("http://www.amazon.com/War-Peace-Leo-Nikolayevich-Tolstoy/dp/1427030200")
# time.sleep(2)
#
# driver.find_element_by_id("img-canvas").click()
# # The easiest way to get exactly one of every page
# imageList = set()
#
# # Wait for the page to load
# time.sleep(10)
# print(driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"))
# while "pointer" in driver.find_element_by_id("sitbReaderRightPageTurner").get_attribute("style"):
#     # While we can click on the right arrow, move through the pages
#     driver.find_element_by_id("sitbReaderRightPageTurner").click()
#     time.sleep(2)
#     # Get any new pages that have loaded (multiple pages can load at once)
#     pages = driver.find_elements_by_xpath("//div[@class='pageImage']/div/img")
#     for page in pages:
#         image = page.get_attribute("src")
#         imageList.add(image)
#
# driver.quit()
#
# # Start processing the images we've collected URLs for with Tesseract
# for image in sorted(imageList):
#     urlretrieve(image, "page.jpg")
#     p = subprocess.Popen(["tesseract", "page.jpg", "page"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#     p.wait()
#     f = open("page.txt", "r")
#     print(f.read())
#
# # 验证码提取
# from urllib.request import urlretrieve
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import subprocess
# import requests
# from PIL import Image
# from PIL import ImageOps
#
#
# def cleanImage(imagePath):
#     image = Image.open(imagePath)
#     image = image.point(lambda x: 0 if x < 143 else 255)
#     borderImage = ImageOps.expand(image, border=20, fill='white')
#     borderImage.save(imagePath)
#
#
# html = urlopen("http://www.pythonscraping.com/humans-only")
# bsObj = BeautifulSoup(html, 'lxml')
# # Gather prepopulated form values
# imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
# formBuildId = bsObj.find("input", {"name": "form_build_id"})["value"]
# captchaSid = bsObj.find("input", {"name": "captcha_sid"})["value"]
# captchaToken = bsObj.find("input", {"name": "captcha_token"})["value"]
#
# captchaUrl = "http://pythonscraping.com" + imageLocation
# urlretrieve(captchaUrl, "captcha.jpg")
# cleanImage("captcha.jpg")
# p = subprocess.Popen(["tesseract", "captcha.jpg", "captcha"], stdout=
# subprocess.PIPE, stderr=subprocess.PIPE)
# p.wait()
# f = open("captcha.txt", "r")
#
# # Clean any whitespace characters
# captchaResponse = f.read().replace(" ", "").replace("\n", "")
# print("Captcha solution attempt: " + captchaResponse)
#
# if len(captchaResponse) == 5:
#     params = {"captcha_token": captchaToken, "captcha_sid": captchaSid,
#               "form_id": "comment_node_page_form", "form_build_id": formBuildId,
#               "captcha_response": captchaResponse, "name": "Ryan Mitchell",
#               "subject": "I come to seek the Grail",
#               "comment_body[und][0][value]":
#                   "...and I am definitely not a bot"}
#     r = requests.post("http://www.pythonscraping.com/comment/reply/10",
#                       data=params)
#     responseObj = BeautifulSoup(r.text, 'lxml')
#     if responseObj.find("div", {"class": "messages"}) is not None:
#         print(responseObj.find("div", {"class": "messages"}).get_text())
# else:
#     print("There was a problem reading the CAPTCHA correctly!")
