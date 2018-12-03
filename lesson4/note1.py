#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/6/20 22:34
"""

## 一个实例认识正则表达式
import re

s = '123abc456eabc789'
re.findall(r'abc', s)
# result: ['abc', 'abc']
re.findall('[0-9]+', s)
# result: ['123', '456', '789']



## 限定符
import re

s = 'Chapter1 Chapter2 Chapter10 Chapter99 fheh'
re.findall('Chapter[1-9][0-9]*', s)
# result:['Chapter1', 'Chapter2', 'Chapter10', 'Chapter99']
re.findall('Chapter[1-9][0-9]+', s)
# result: ['Chapter10', 'Chapter99']
re.findall('Chapter[1-9][0-9]?', s)
# result:['Chapter1', 'Chapter2', 'Chapter10', 'Chapter99']
re.findall('Chapter[1-9][0-9]{0,1}', s)
# result:['Chapter1', 'Chapter2', 'Chapter10', 'Chapter99']
re.findall('Chapter[1-9][0-9]{1,2}', s)
# result:['Chapter10', 'Chapter99']

## 贪婪模式与非贪婪模式
import re

# 贪婪模式
s = '<H1>Chapter 1 – Introduction to Regular Expressions</H1>'
re.findall('<.*>', s)
# result: ['<H1>Chapter 1 – Introduction to Regular Expressions</H1>']
# 非贪婪模式
re.findall('<.*?>', s)
# result: ['<H1>', '</H1>']


## 定位符
import re

s = 'Chapter1 Chapter2 Chapter11 Chapter99'
re.findall('^Chapter[1-9][0-9]{0,1}', s)
# result: ['Chapter1']
re.findall('^Chapter[1-9][0-9]{0,1}$', 'Chapter99')
# result: ['Chapter99']
re.findall(r'\bCha', ' Chapter')
# result: ['Cha']
re.findall(r'ter\b', ' Chapter')
# result: ['ter']
re.findall(r'\Bapt', 'Chapter')
# result: ['apt']
re.findall(r'\Bapt', 'aptitude')
# result: []


# 分组与捕获组
"""
要说明白捕获，就要先从分组开始。
重复单字符我们可以使用限定符，如果重复字符串，用什么呢？ 
对！用小括号，小括号里包裹指定字表达式（子串），这就是分组。之后就可以限定这个子表示的重复次数了。

那么，什么是捕获呢？
使用小括号指定一个子表达式后，匹配这个子表达式的文本（即匹配的内容）可以在表达式或者其他过程中接着用，怎么用呢？
至少应该有个指针啥的引用它吧？
 对！默认情况下，每个分组（小括号）会自动拥有一个组号,从左到右，以分组的左括号为标志，第一个出现的分组组号为1，后续递增。如果出现嵌套，
"""
s = 'aaa111aaa , bbb222 , 333ccc'
re.findall(r'[a-z]+(\d+)[a-z]', s)
# result:['111']
re.findall(r'[a-z]+\d+[a-z]', s)  # 对比(\d+)的用法
# result:['aaa111a']
re.findall(r'[a-z]+\d+[a-z]+', s)  # 对比(\d+)的用法
# result:['aaa111aaa']

s = '111aaa222aaa111 , 333bbb444bb33'
re.findall(r'(\d+)([a-z]+)(\d+)(\2)(\1)', s)
# result:[('111', 'aaa', '222', 'aaa', '111')]
re.findall(r'(\d+)([a-z]+)(\d+)(\2)(\1)', '333bbb444bb33')
# result:[]
re.findall(r'(\d+)([a-z]+)(\d+)(\2)(\1)', '333bbb444bbb333')
# result:[('333', 'bbb', '444', 'bbb', '333')]
re.findall(r'(\d+)([a-z]+)(\d+)(\1)(\2)', '333bbb444bbb333')
# result:[]


## 非捕获组
"""
用圆括号将所有选择项括起来，相邻的选择项之间用|分隔。
但用圆括号会有一个副作用，使相关的匹配会被缓存。
可用?:放在第一个选项前来消除这种副作用。

其中 ?: 是非捕获元之一，还有两个非捕获元是 ?= 和 ?!，这两个还有更多的含义，
前者为正向预查，在任何开始匹配圆括号内的正则表达式模式的位置来匹配搜索字符串，
后者为负向预查，在任何开始不匹配该正则表达式模式的位置来匹配搜索字符串。
"""
# (?:pattern)与(pattern)不同之处只是在于不捕获结果，非捕获组只匹配结果，但不捕获结果，也不会分配组号
s = 'industry is industries lala industyyy industiii'
re.findall(r'industr(?:y|ies)', s)
# result: ['industry', 'industries']

s = 'Windows2000 Windows3.1'
re.findall(r'Windows(?=95|98|NT|2000)', s)
# result: ['Windows']
# 匹配 "Windows2000" 中的 "Windows",不匹配 "Windows3.1" 中的 "Windows"。

s = 'Windows2000 Windows3.1'
re.findall(r'Windows(?!95|98|NT|2000)', s)
# result: ['Windows']
# 匹配 "Windows3.1" 中的 "Windows",不匹配 "Windows2000" 中的 "Windows"。

s = 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777ggg'
re.findall(r'([a-z]+)\d+([a-z]+)', s)
# result:[('aaa', 'aaa'), ('fff', 'ggg')]
re.findall(r'(?P<g1>[a-z]+)\d+(?P=g1)', s)
# result:['aaa']
re.findall(r'(?P<g1>[a-z]+)\d+(?P=g1)', 'aaa111aaa,bbb222,333ccc,444ddd444,555eee666,fff777fff')
# result:['aaa', 'fff']
re.findall(r'[a-z]+(\d+)([a-z]+)', s)
# result: [('111', 'aaa'), ('777', 'ggg')]
re.findall(r'([a-z]+)\d+', s)
# result:['aaa', 'bbb', 'ddd', 'eee', 'fff']
re.findall(r'([a-z]+)\d+\1', s)
# result:['aaa']

s = 'I have a dog , I have a cat'
re.findall(r'I have a (?:dog|cat)', s)
# result: ['I have a dog', 'I have a cat']
re.findall(r'I have a dog|cat', s)
# result: ['I have a dog', 'cat']

s = 'ababab abbabb aabaab abbbbbab'
re.findall(r'\b(?:ab)+\b', s)
# result: ['ababab']
re.findall(r'\b(ab)+\b', s)
# result: ['ab']


# 反向引用
"""
捕获组在匹配成功时，会将子表达式匹配到的内容，保存到内存中一个以数字编号的组里，
可以简单的认为是对一个局部变量进行了赋值，这时就可以通过反向引用方式，引用这个局部变量的值。
一个捕获组在匹配成功之前，它的内容可以是不确定的，一旦匹配成功，它的内容就确定了，反向引用的内容也就是确定的了。

反向引用必然要与捕获组一同使用的，
如果没有捕获组，而使用了反向引用的语法，不同语言的处理方式不一致，有的语言会抛异常，有的语言会当作普通的转义处理。
"""
s = 'Is is the cost of of gasoline going up up ?'
re.findall(r'\b([a-z]+) \1\b', s, re.I)  # 大小写不敏感
# result: ['Is', 'of', 'up']
re.findall(r'\b([a-z]+) \1\b', s)
# result: ['of', 'up']

s = 'http://www.w3cschool.cc:80/html/html-tutorial.html'
re.findall(r'(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)', s)
# result: [('http', 'www.w3cschool.cc', ':80', '/html/html-tutorial.html')]



## 基本匹配模式
s1 = "once upon a time"
s2 = "There once was a man from NewYork"
print(re.findall(r'^once', s1))
# result: ['once']
print(re.findall(r'^once', s2))
# result: []
print(re.findall(r'time$', s1))
# result: ['time']
print(re.findall(r'times$', s1))
# result: []
print(re.findall(r'^time$', s1))
# result: []
print(re.findall(r'^time$', 'time'))
# result: ['time']

## compile
s = '111,222,aaa,bbb,ccc333,444ddd'
rule = r'\b\d+\b'
compiled_rule = re.compile(rule)
print(compiled_rule.findall(s))
# result: ['111', '222']


## match
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
# result: (0, 3)
print(re.match('com', 'www.runoob.com'))  # 不在起始位置匹配
# result: None

line = "Cats are smarter than dogs"
matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    # result: matchObj.group() :  Cats are smarter than dogs
    print("matchObj.group(1) : ", matchObj.group(1))
    # result: matchObj.group(1) :  Cats
    print("matchObj.group(2) : ", matchObj.group(2))
    # result: matchObj.group(2) :  smarter
else:
    print("No match!!")

## search
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# result: (0, 3)
print(re.search('com', 'www.runoob.com').span())  # 不在起始位置匹配
# result: (11, 14)

line = "Cats are smarter than dogs";
searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    # result: searchObj.group() :  Cats are smarter than dogs
    print("searchObj.group(1) : ", searchObj.group(1))
    # result: searchObj.group(1) :  Cats
    print("searchObj.group(2) : ", searchObj.group(2))
    # result: searchObj.group(2) :  smarter
else:
    print("Nothing found!!")

## match与search
line = "Cats are smarter than dogs"
matchObj = re.match(r'dogs', line, re.M | re.I)

if matchObj:
    print("match --> matchObj.group() : ", matchObj.group())
else:
    print("No match!!")
    # result: No match!!

matchObj = re.search(r'dogs', line, re.M | re.I)
if matchObj:
    print("search --> matchObj.group() : ", matchObj.group())
    # result: search --> matchObj.group() :  dogs
else:
    print("No match!!")

## sub
phone = "2004-959-559 # This is Phone Number"
num = re.sub(r'#.*$', "", phone)
print("Phone Num : ", num)
# result: Phone Num :  2004-959-559

num = re.sub(r'\D', "", phone)
print("Phone Num : ", num)
# result: Phone Num :  2004959559


## 正则表达式与BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, 'lxml')
# print(bsObj.prettify())
images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    print(image["src"])

# result: ../img/gifts/img1.jpg
# ../img/gifts/img2.jpg
# ../img/gifts/img3.jpg
# ../img/gifts/img4.jpg
# ../img/gifts/img6.jpg