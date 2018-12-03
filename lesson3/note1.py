#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/6/18 1:27
"""

# 最基本的方法打开网页
from urllib.request import urlopen

response = urlopen("http://www.baidu.com")
print(type(response))
print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
html = response.read()
print(html)

# 携带data参数打开网页
from urllib.parse import urlencode
from urllib.request import urlopen

data = bytes(urlencode({'word': 'hello'}), encoding='utf8')
response = urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

#  携带timeout参数打开网页1
from urllib.request import urlopen

# response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
response = urlopen('http://httpbin.org/get', timeout=1)
print(response.read())

# 携带timeout参数打开网页2
from urllib.request import urlopen

try:
    response = urlopen('http://httpbin.org/get', timeout=0.1)
    print(response.read())
except Exception as e:
    print(e)

# 通过构建Request打开网页1
from urllib.request import Request
from urllib.request import urlopen

request = Request('https://python.org')
response = urlopen(request)
print(response.read().decode('utf-8'))

# 通过构建Request打开网页2
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0(compatibe;MSIE 5.5;Windows NT)',
    'Host': 'httpbin.org'
}
dict = {'name': 'Germey'}
data = bytes(urlencode(dict), encoding='utf8')
req = Request(url=url, data=data, headers=headers, method='POST')
response = urlopen(req)
print(response.read().decode('utf-8'))

# 与通过构建Request打开网页2对比
from urllib.request import Request
from urllib.request import urlopen

req = Request(url=url, data=data, method='POST')
response = urlopen(req)
print(response.read().decode('utf-8'))

# 通过构建Request打开网页3：通过add_header方法添加headers
from urllib.request import Request
from urllib.request import urlopen
from urllib.parse import urlencode

url = 'http://httpbin.org/post'
dict = {'name': 'Germey'}
data = bytes(urlencode(dict), encoding='utf8')
req = Request(url=url, data=data, method='POST')
req.add_header('User-Agent', 'Mozilla/4.0(compatibe;MSIE 5.5;Windows NT)')
response = urlopen(req)
print(response.read().decode('utf-8'))

# urlencode()的使用
from urllib.parse import urlencode
from urllib.request import urlopen

data = {'first': 'true', 'pn': 1, 'kd': 'Python'}
data = urlencode(data).encode('utf-8')
data
page = urlopen(req, data=data).read()
page

# 使用代理
from urllib.error import URLError
from urllib.request import ProxyHandler, build_opener

proxy_handler = ProxyHandler({'http': '106.56.102.140:8070'})
opener = build_opener(proxy_handler)
try:
    response = opener.open('http://www.baidu.com/')
    print(response.read().decode('utf-8'))
except URLError as e:
    print(e.reason)
