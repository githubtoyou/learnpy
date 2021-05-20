# -*- coding = utf-8 -*-
# @Time:2021/5/1415:04
# @Author:Charlie
# @File:zodiac.py
# @Software:PyCharm
# Ctrl + D           复制选定的区域或行到后面或下一行
# Shift + Enter      下一行另起一行
# Ctrl + Delete      删除到字符结束--->往后删除全部
# Ctrl + Backspace    删除到字符开始《----往前删除全部
# Ctrl + /           行注释（可选中多行
import os
import types
import logging
import pdb
import sys
import functools
import unittest

# c = 'zyx'
# cz_num = {}
# for i in c:
#     cz_num[i] = 0
# print(cz_num)

# file1 = open('name.txt', 'w')
# file1.write('laozhu')
# file1.close()
# print(file1)

# file2= open('name.txt', 'r')
# print(file2.read())
# print(file2.readlines())
# file2.close()


# print(file2.tell())
# print(file2.read(1))
# file2.seek(0)
# print(file2.tell())

# def fun2(item):
#     return item[0]
#
# adict = {'a':'aa', 'b':'bb'}
# for i in adict.items():
#     fun2(i)
# for i in zip((1,2,3),(4,5,6)):
#     print(i)

# def counter():
#     cnt = [0]
#     def add_one():
#         cnt[0] += 1
#         print(cnt)
#
#
#      return add_one
# counter()
# cnt = [1]
# print(cnt[0])
# print(cnt)
#
# cnt[0] = + 1 + 1
# print(cnt[0])

# /dev/peps/pep-0008

# class Testwith():
#     def __enter__(self):
#         print('run')
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print('exit')
# with Testwith():
#     print('Test is running')

# import queue
# q = queue.Queue()
# q.put(1)
# q.put(2)
# q.put(3)
# q.get()


import  re
# p = re.compile('a')
# print(p.match('b'))

phone = '123-456-789 # zheshidianhuahaoma'
p2 = re.sub(r' #.*$','',phone)
print(p2)

