#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/7/27 11:04
"""
import requests
import json
import time
import random
import pymysql.cursors


def crawlDetailPage(url, page):
    # 读取微博网页的JSON信息
    req = requests.get(url)
    jsondata = req.text
    data = json.loads(jsondata)

    # 获取每一条页的数据
    content = data['cards']
    # print(content)

    # 循环输出每一页的关注者各项信息
    for i in content:
        followingId = i['user']['id']
        followingName = i['user']['screen_name']
        followingUrl = i['user']['profile_url']
        followersCount = i['user']['followers_count']
        followCount = i['user']['follow_count']
        followCount = i['user']['location']

        print("---------------------------------")
        print("用户ID为:{}".format(followingId))
        print("用户昵称为:{}".format(followingName))
        print("用户详情链接为:{}".format(followingUrl))
        print("用户粉丝数:{}".format(followersCount))
        print("用户关注数:{}".format(followCount))
        print("用户地址:{}".format(followCount))

        '''
        数据库操作
        '''

        # 获取数据库链接
        connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='123456',
                                     db='weibo',
                                     charset='utf8mb4')
        try:
            # 获取会话指针
            with connection.cursor() as cursor:
                # 创建sql语句
                sql = "insert into `following` (`followingId`,`followingName`,`followingUrl`,`followersCount`,`followCount`) values (%s,%s,%s,%s,%s)"

                # 执行sql语句
                cursor.execute(sql, (followingId, followingName, followingUrl, followersCount, followCount))

                # 提交数据库
                connection.commit()
        finally:
            connection.close()


for i in range(1, 11):
    print("正在获取第{}页的关注列表:".format(i))
    # 微博用户关注列表JSON链接
    url = "https://m.weibo.cn/api/container/getSecond?containerid=1005052164843961_-_FOLLOWERS&page=" + str(i)
    crawlDetailPage(url, i)
    # 设置休眠时间
    t = random.randint(31, 33)
    print("休眠时间为:{}s".format(t))
    time.sleep(t)
