#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:note2.py
@time:2018/8/28 14:44
"""
''' JSON数据的解析 '''
import json

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},{"fruit":"banana"},{"fruit":"pear"}]}'
jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[1])
print(jsonObj.get("arrayOfNums")[1].get("number") + jsonObj.get("arrayOfNums")[2].get("number"))
print(jsonObj.get("arrayOfFruits")[2].get("fruit"))

''' 聚合数据 天气预报API '''
from urllib import urlencode
import urllib
import json

# 配置您申请的APPKey
appkey = "84bd1042092e7b0e3265483f46febc80"


# 根据城市查询天气
def queryWeather(appkey, m="GET", city="广州", dtype="json"):
    url = "http://v.juhe.cn/weather/index"
    params = {
        "cityname": city,  # 要查询的城市，如：温州、上海、北京
        "key": appkey,  # 应用APPKEY(应用详细页查询)
        "dtype": dtype,  # 返回数据的格式,xml或json，默认json
    }
    params = urlencode(params, )
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            return res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


weather = queryWeather(appkey, "GET")
print weather
print urllib.unquote(weather.get("sk").get("wind_direction"))

''' 聚合数据 IP地址查询API '''
from urllib import urlopen
import json


def getCountry(ipAddress, appkey):
    response = urlopen("http://apis.juhe.cn/ip/ip2addr?ip=" + ipAddress + "&key=" + appkey).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("area")


# 配置您申请的APPKey
appkey = "84bd1042092e7b0e3265483f46febc80"
print(getCountry("61.135.169.121", appkey))
