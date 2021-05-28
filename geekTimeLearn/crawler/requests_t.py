# -*- coding = utf-8 -*-
# @Time:2021/5/2014:33
# @Author:Charlie
# @File:requests_t.py
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
# import  requests
# url = 'http://httpbin.org/get'
# data = {'key':'value','abc':'zyx'}
# response = requests.get(url, data)
# print(response.text)

import  requests
url = 'http://httpbin.org/post'
data = {'key':'value','abc':'zyx'}
response = requests.post(url, data)
print(response.json())