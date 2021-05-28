
# -*- coding = utf-8 -*-
# @Time:2021/5/2012:01
# @Author:Charlie
# @File:requests_headers.py
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
from urllib import request, parse
url = 'http://httpbin.org/post'

headers =  {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
"Host": "httpbin.org",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
"X-Amzn-Trace-Id": "Root=1-60a5db57-012fb7db7451e7d61e68673d"
}
dict={
'name':'value'
}
data = bytes(parse.urlencode(dict), encoding='utf-8') #封装和编码转换
req = request.Request(url=url, data=data, headers= headers,method='POST')
response = request.urlopen(req) #打开网页
print(response.read().decode('utf-8')) #读取网页
