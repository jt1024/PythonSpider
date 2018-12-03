#!/usr/bin/python
# encoding:utf-8

"""
@author:jiat
@contact:cctvjiatao@163.com
@file:homework.py
@time:2018/6/17 21:51
"""

# 键盘输入（python3将raw_input和input进行了整合，只有input）
str = input("Please enter:")
print("你输入的内容是：", str)

# 打开一个文件
fo = open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "wb")
print("文件名：", fo.name)
print("是否已关闭：", fo.closed)
print("访问模式：", fo.mode)

# 关闭一个文件
fo = open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "wb")
fo.close()
print("是否已关闭：", fo.closed)

# 写入文件内容
fo = open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "r+")
fo.write("www.baidu.com www.cctvjiatao.com")
fo.flush()
fo.close()

# 读取文件内容
fo = open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "r+")
str = fo.read(11)
print("读取的字符串是：", str)
fo.close()

# 查找当前位置
fo = open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "r+")
str = fo.read(11)
position = fo.tell()
print("当前读取的位置是：", position)
# result: 当前文件位置： 11
fo.close()

# 文件指针重定位
fo = open(r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt", "r+")
str = fo.read(11)
print("读取的字符串1：", str)
# result: 重新读取的字符串1： www.baidu.c
position = fo.tell()
print("当前文件位置：", position)
# result: 当前文件位置： 11
str = fo.read(11)
print("读取的字符串2：", str)
# result: 读取的字符串2： om www.cctv
postion = fo.seek(0, 0)
str = fo.read(11)
print("读取的字符串3：", str)
# result: 读取的字符串3： www.baidu.c
fo.close()

# 文件重命名 filejiatao.txt——>filejiatao2.txt
import os

src_file = r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao.txt"
dst_file = r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao2.txt"
os.rename(src_file, dst_file)

# 删除一个文件
import os

dirty_file = r"D:\DataguruPyhton\PythonSpider\lesson2\filejiatao2.txt"
os.remove(dirty_file)

# 异常处理1
try:
    fh = open("testfile.txt", "w")
    fh.write("this is my test file for exception handing!")
except IOError:
    print("Eorror:can\'t find file or read data")
else:
    print("witten content in the file successfully")
    fh.close()

# 异常处理2
try:
    fh = open("testfile.txt", "w")
    fh.write("this is my test file for exception handing!")
finally:
    print("Eorror:I don\'t kown why ...")


# 异常处理3
def temp_convert(var):
    try:
        return int(var)
    # except ValueError,Argument:
    #     print("The argument does not contain numbers\n",Argument)
    except (ValueError) as Argument:
        print("The argument does not contain numbers\n", Argument)


temp_convert("xyz")
