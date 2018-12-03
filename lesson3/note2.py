#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/6/18 8:04
"""

########### requests.request 的用法 ############

## request(method, url, **kwargs)，当 **kwargs 为 params
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('GET', 'http://httpbin.org/get', params=payload)
print(r.url)
# result: http://httpbin.org/get?key1=value1&key2=value2
print(r.text)
# result:
# {
#   "args": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.19.1"
#   },
#   "origin": "1.203.183.95",
#   "url": "http://httpbin.org/get?key1=value1&key2=value2"
# }


## request(method, url, **kwargs)，当 **kwargs 为 data
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('POST', 'http://httpbin.org/post', data=payload)
print(r.url)
# result: http://httpbin.org/post
print(r.text)
# result:
# {
#   "args": {},
#   "data": "",
#   "files": {},
#   "form": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "23",
#     "Content-Type": "application/x-www-form-urlencoded",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.19.1"
#   },
#   "json": null,
#   "origin": "1.203.183.95",
#   "url": "http://httpbin.org/post"
# }


## request(method, url, **kwargs)，当 **kwargs 为 json
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.request('POST', 'http://httpbin.org/post', json=payload)
print(r.url)
# result: http://httpbin.org/post
print(r.text)
# result:
# {
#   "args": {},
#   "data": "{\"key1\": \"value1\", \"key2\": \"value2\"}",
#   "files": {},
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "36",
#     "Content-Type": "application/json",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.19.1"
#   },
#   "json": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "origin": "1.203.183.95",
#   "url": "http://httpbin.org/post"
# }


## request(method, url, **kwargs)，当 **kwargs 为 headers
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
r = requests.request('GET', 'http://httpbin.org/get', params=payload, headers=headers)
print(r.url)
# result: http://httpbin.org/get?key1=value1&key2=value2
print(r.text)
# result:
# {
#   "args": {
#     "key1": "value1",
#     "key2": "value2"
#   },
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"
#   },
#   "origin": "1.203.183.95",
#   "url": "http://httpbin.org/get?key1=value1&key2=value2"
# }


## request(method, url, **kwargs)，当 **kwargs 为 cookies
import requests

cookies = dict(cookies_are='working')
r = requests.request('GET', 'http://httpbin.org/cookies', cookies=cookies)
print(r.url)
# result: http://httpbin.org/cookies
print(r.text)
# result:
# {
#   "cookies": {
#     "cookies_are": "working"
#   }
# }


## request(method, url, **kwargs)，当 **kwargs 为 auth
import requests

cs_user = '用户名'
cs_psw = '密码'
r = requests.request('GET', 'https://api.github.com', auth=(cs_user, cs_psw))
print(r.url)
# result: 待补充
print(r.text)
# result: 待补充


## request(method, url, **kwargs)，当 **kwargs 为 file
import requests

files = {'file': open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "rb")}
r = requests.request('POST', 'http://httpbin.org/post', files=files)
print(r.url)
# result: http://httpbin.org/post
print(r.text)
# result:
# {
#   "args": {},
#   "data": "",
#   "files": {
#     "file": "www.baidu.com www.cctvjiatao.com"
#   },
#   "form": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Content-Length": "182",
#     "Content-Type": "multipart/form-data; boundary=ee12ea6a4fd2b8a3318566775f2b268f",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.19.1"
#   },
#   "json": null,
#   "origin": "1.203.183.95",
#   "url": "http://httpbin.org/post"
# }


## request(method, url, **kwargs)，当 **kwargs 为 timeout
import requests

r = requests.request('GET', 'http://github.com', timeout=0.001)
print(r.url)
# result: 报错 socket.timeout: timed out


## request(method, url, **kwargs)，当 **kwargs 为 proxies
import requests

proxies = {
    'https': 'http://41.118.132.69:4433'
}
# 也可以通过环境变量设置代理
# export HTTP_PROXY='http://10.10.1.10:3128'
# export HTTPS_PROXY='http://10.10.1.10:1080'
r = requests.request('GET', 'http://httpbin.org/get', proxies=proxies)
print(r.url)
# result: http://httpbin.org/get
print(r.text)
# result:
# {
#   "args": {},
#   "headers": {
#     "Accept": "*/*",
#     "Accept-Encoding": "gzip, deflate",
#     "Connection": "close",
#     "Host": "httpbin.org",
#     "User-Agent": "python-requests/2.19.1"
#   },
#   "origin": "1.203.183.95",
#   "url": "http://httpbin.org/get"
# }


## request(method, url, **kwargs)，当 **kwargs 为 verify，SSL证书验证
import requests

r = requests.request('GET', 'https://kyfw.12306.cn/otn/', verify=True)
print(r.text)

r = requests.request('GET', 'https://kyfw.12306.cn/otn/', verify=False)
print(r.text)

r = requests.request('GET', 'https://github.com', verify=True)
print(r.text)

################################################################################################



########### requests 的其他方法  ############
import requests
import json

# url下载
r = requests.get('http://cuiqingcai.com')
print(type(r))
print(r.status_code)
print(r.encoding)
print(r.cookies)
requests.request()
# 基本请求
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# get请求
r = requests.get('http://httpbin.org/get')
print(r.url)
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

# 获得原始的套接字
r = requests.get('https://github.com/timeline.json', stream=True)
r.raw

payload = {'key1': 'value1', 'key2': 'value2'}
headers = {'content-type': 'application/json'}
r = requests.get('http://httpbin.org/get', params=payload, headers=headers)
print(r.url)

# post请求1-提交表单形式的参数
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post('http://httpbin.org/post', data=payload)
print(r.text)

# post请求2-提交json形式的参数
payload = {'some': 'data'}
r = requests.post('http://httpbin.org/post', data=json.dumps(payload))
print(r.text)

# post请求3-提交file形式的参数
files = {'file': open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "rb")}
r = requests.post('http://httpbin.org/post', files=files)
print(r.text)

# Cookies
url = 'http://httpbin.org/cookies'
cookies = dict(cookies_are='working')
r = requests.get(url, cookies=cookies)
print(r.text)

# 超时配置
requests.get('http://github.com', timeout=0.001)

# 会话对象
requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)
# result: {"cookies":{}}

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/1234')
r = s.get('http://httpbin.org/cookies')
print(r.text)
# result: {"cookies":{"sessioncookie":"1234"}}

s = requests.Session()
s.headers.update({'x=test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test2': 'true'})
print(r.text)

r = s.get('http://httpbin.org/headers', headers={'x-test': 'true'})
r = s.get('http://httpbin.org/headers', headers={'x-test': None})

# SSL证书验证
r = requests.get('https://kyfw.12306.cn/otn/', verify=True)
print(r.text)

r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print(r.text)

r = requests.get('https://github.com', verify=True)
print(r.text)

# 代理
proxies = {
    'https': 'http://41.118.132.69:4433'
}
r = requests.post('http://httpbin.org/post', proxies=proxies)
print(r.text)

# #通过环境变量设置代理
# export HTTP_PROXY='http://10.10.1.10:3128'
# export HTTPS_PROXY='http://10.10.1.10:1080'


# requests库的异常处理
try:
    r = requests.get(url, timeout=30)  # 请求超时时间为30秒
    r.raise_for_status()  # 如果状态不是200，则引发异常
    r.encoding = r.apparent_encoding  # 配置编码
    print(r.text)
except:
    print("产生异常")

######################## 实例运用 ###############################################
## 京东商品信息的爬取
# 不需要对头部做任何修改，即可爬网页
import requests

url = 'http://item.jd.com/2967929.html'
try:
    r = requests.get(url, timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[:1000])  # 部分信息
except:
    print("失败")

## 亚马逊商品信息的爬取
# 该网页中对爬虫进行的爬取做了限制，因此我们需要伪装自己为浏览器发出的请求
import requests

url = 'http://www.amazon.cn/gp/product/B01M8L5Z3Y'
try:
    kv = {'user_agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)  # 改变自己的请求数据
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])  # 部分信息
except:
    print("失败")

## 百度搜索关键字提交
# 百度的关键字接口：https://www.baidu.com/s?wd=keyword
import requests

keyword = 'python'
try:
    kv = {'wd': keyword}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}
    r = requests.get('https://www.baidu.com/s', params=kv, headers=headers)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    # print(len(r.text))
    print(r.text)
except:
    print("失败")

## 网络图片的爬取
import requests
import os

try:
    url = "https://odonohz90.qnssl.com/library/145456/bb0b3faa7a872d012bb4c57256b47585.jpg?imageView2/2/w/1000/h/1000/q/75"  # 图片地址
    root = r"D:\DataguruPyhton\PythonSpider\lesson3\pic\\"
    path = root + url.split("/")[-1]
    if not path.endswith(".jpg"):
        path += ".jpg"
    if not os.path.exists(root):  # 目录不存在创建目录
        os.mkdir(root)
    if not os.path.exists(path):  # 文件不存在则下载
        r = requests.get(url)
        f = open(path, "wb")
        f.write(r.content)
        f.close()
        print("文件下载成功")
    else:
        print("文件已经存在")
except:
    print("获取失败")
