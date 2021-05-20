#-*- coding = utf-8 -*-
#@Time:2021/5/1316:27
#@Author:Charlie
#@File:contestlib_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest

# try :
#     f= open('F:\learnpy\IOprogram\io.txt', 'r')
#     p = f.read()
#     print(p)
# finally:
#     if f:
#         f.close()
# with open('F:\learnpy\IOprogram\io.txt', 'r') as f:
#     print(f.read())

# class Query(object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Begin')
#         return self
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#
#     def query(self):
#         print('Query info about %s...' % self.name)
#
# with Query('Bob') as q:
#     q.query()

# from contextlib import contextmanager
# @contextmanager
# def tag(name):
#     print("<%s>" % name)
#     yield
#     print("</%s>" % name)
# with tag("h1"):
#     print("hello")
#     print("world")

from contextlib import closing
from urllib.request import urlopen
with closing(urlopen('https://www.baidu.com')) as page:
    for line in page:
        print(line)