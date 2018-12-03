#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/7/16 0:29
"""

import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
# 直接输入的初始网址
star_url = 'http://www.dangdang.com/'
# 汉语 在输入狂中要查找的关键字
keys = ('汉语').decode('utf-8')


def open_page():
    try:
        driver.get(star_url)
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key_S')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button")))
        input.send_keys(keys)
        submit.click()
    except TimeoutException:
        open_page()


def get_contents():
    try:
        html = driver.page_source
        pattern = re.compile(r'<li.*?data-original="(.*?)".*?alt="(.*?)".*?class="price_n">(.*?)</span>.*?class="level".*?_1_q">(.*?)</a>.*?</li>', re.S)
        items = re.findall(pattern, html)
        for item in items:
            img, name, price, num = item
            print
            img, name, price, num
    except TimeoutException:
        get_contents()


def next_page(page):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#t__cp')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#click_get_page")))
        input.clear()
        input.send_keys(page)
        submit.click()
        get_contents()
    except TimeoutException:
        next_page(page)


def main():
    open_page()
    get_contents()
    for page in range(2, 101):
        next_page(page)


if __name__ == '__main__':
    main()
