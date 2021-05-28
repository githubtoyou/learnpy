# -*- coding = utf-8 -*-
# @Time:2021/5/2010:45
# @Author:Charlie
# @File:networkLib.py
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
#urllib 收集和下载
#格式处理

from urllib import parse #handel data
from urllib import request  #qingqiu
# url = 'http://www.baidu.com'
# response = request.urlopen(url, timeout=1)
# print(response.read().decode('utf-8'))

# response2 = request.urlopen('http://httpbin.org/get', timeout=1)
# print(response2.read())

data = bytes(parse.urlencode({'world':'hello'}),encoding='utf-8')
response = request.urlopen('http://httpbin.org/post', data=data)
print(response.read().decode('utf-8'))

# import socket
# import urllib
# try:
#     response3 = request.urlopen('http://httpbin.org/get', timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason, socket.timeout):
#         print('TIME OUT')