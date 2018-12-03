#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note3.py
@time:2018/8/29 6:52
"""

''' python3.x 调用 微博 API '''
## weibo sdk下载地址 https://github.com/nooperpudd/weibopy
from weibopy import WeiboOauth2
import webbrowser

## 1、个人微博的账号信息
APP_KEY = '2337575664'
APP_SECRET = '84962fa90b235df7a06e71b495cd04ca'
CALLBACK_URL = 'http://f.dataguru.cn'

## 2、请求授权
# 2.1
client = WeiboOauth2(APP_KEY, APP_SECRET, CALLBACK_URL)
authorize_url = client.authorize_url
print(authorize_url)
# https://api.weibo.com/oauth2/authorize?redirect_uri=http%3A//f.dataguru.cn&response_type=code&client_id=2337575664
# 2.2
# 打开申请授权的网页，点击同意授权后会跳转到之前设置的回调网页（即CALLBACK_URL）
# 在回调页的浏览器地址栏里获取code（动态变化），用于第二步调用oauth2/access_token接口，获取授权后的access token
webbrowser.open_new(authorize_url)
# http://f.dataguru.cn/?code=4b156593e9dfdd16279bbcc9eb7817bf
code = '4b156593e9dfdd16279bbcc9eb7817bf'

## 3、获得授权
# 获取token 和 token的生命周期
r = client.auth_access(code)
# print(r)
# {'access_token': u'2.0053aLTGSNOMYCc0217260bahxd6uC', 'expires': 1693066525, 'expires_in': 1693066525, 'uid': u'5928072116'}
access_token = r.get("access_token")
# print(access_token)
# 2.0053aLTGSNOMYCc0217260bahxd6uC
expires_in = r.expires_in
# print(expires_in)
# 1693066525

## 4、为以后的API请求设置token
from weibopy import WeiboClient

client = WeiboClient(access_token)

## 5、获取当前登录用户及其所关注（授权）用户的最新微博 statuses/home_timeline
# https://api.weibo.com/2/statuses/home_timeline.json
result = client.get(suffix="statuses/home_timeline.json")
statuses = result.get("statuses")
# print(statuses[0])
length = len(statuses)
print(length)
# 输出了部分信息
for i in range(0, length):
    print(u'昵称：' + statuses[i]['user']['screen_name'])
    print(u'简介：' + statuses[i]['user']['description'])
    print(u'位置：' + statuses[i]['user']['location'])
    print(u'微博：' + statuses[i]['text'])

## 6、获取最新的提到登录用户的微博列表，即@我的微博 statuses/mentions
# https://api.weibo.com/2/statuses/mentions.json
result = client.get(suffix="statuses/mentions.json")
statuses = result.get("statuses")
# print(statuses[0])
length = len(statuses)
print(length)
# 输出了部分信息
for i in range(0, length):
    print(u'昵称：' + statuses[i]['user']['screen_name'])
    print(u'简介：' + statuses[i]['user']['description'])
    print(u'位置：' + statuses[i]['user']['location'])
    print(u'微博：' + statuses[i]['text'])
    print(u'时间：' + statuses[i]['created_at'])
