#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note3.py
@time:2018/8/12 18:30
"""
"""爬取京东的商品评论(通过封装函数的形式)"""
from selenium import webdriver
from urllib.parse import quote
import pandas as pd
from selenium.common.exceptions import StaleElementReferenceException


def get_page_comment(driver):
    try:
        content = driver.find_elements_by_xpath('//*[@id="comment-0"]//div/div[2]/p')
        content_list = [c.text for c in content]
    except StaleElementReferenceException as msg:
        print(u"get_page_comment异常%s" % msg)
        print(u"重新get_page_comment")
        content = driver.find_elements_by_xpath('//*[@id="comment-0"]//div/div[2]/p')
        content_list = [c.text for c in content]
    return content_list


def get_page_all_comment(driver, i):
    all_content = get_page_comment(driver)
    while True:
        try:
            driver.find_element_by_link_text('下一页').click()
            all_content = all_content + get_page_comment(driver)
        except:
            print("没有下一页了 - " + str(i))  # TODO 点击下一页，获取失败，待优化
            break
    return all_content


def get_all_comment(urls, driver, outpath='D:/DataguruPyhton/PythonSpider/images/'):
    i = 0
    for url in urls:
        i += 1
        driver.get(url)
        driver.find_element_by_xpath('//*[@id="detail"]/div[1]/ul/li[5]').click()  # 点击商品详情
        name = driver.find_element_by_xpath('/html/body/div[8]/div/div[2]/div[1]').text
        print("文件%d - %s" % (i, name))
        comment = get_page_all_comment(driver, i)
        comment = pd.DataFrame(comment)
        comment.to_csv(outpath + str(i) + '.csv')
    return None


def get_links(key, driver):
    url = 'https://search.jd.com/Search?keyword=' + quote(key) + '&enc=utf-8'  # 构造url
    driver.get(url)  # 打开url
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')  # 滚动到页面底部
    driver.implicitly_wait(3)  # 等待
    links = driver.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li/div/div[1]/a')  # 查找当前页面的商品链接
    urls = [l.get_attribute('href') for l in links]
    return urls


def main(key):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # 设置headless模型
    driver = webdriver.Chrome(chrome_options=chrome_options)
    urls = get_links(key, driver)
    get_all_comment(urls, driver, outpath='D:/DataguruPyhton/PythonSpider/images/')


main('红酒')
