# -*- coding = utf-8 -*-
# @Time:2021/5/2014:56
# @Author:Charlie
# @File:crawler_t.py
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
import requests
import re
from bs4 import BeautifulSoup
#url = 'http://www.cnu.cc/discoveryPage/hot-人像'
#url = 'https://movie.douban.com/'


#<div class="grid-item work-thumbnail">
#<a href="http://www.cnu.cc/works/527379" class="thumbnail" target="_blank">
#<div class="title">蓝色魅影</div>
#<div class="author">未央久陌生</div>

# pattern = re.compile(r'<a href="(.*?)".*?title">(.*?)</div>', re.S)
# results = re.findall(pattern, content)
# # print(results)
# for result in results:
#     url, name = result
#     print(url, re.sub('\s', '',name))


url = 'https://www.baidu.com'
html = requests.get(url)
html.encoding = 'utf-8'
soup = BeautifulSoup(html.text,'lxml')
#print(soup.prettify()) #返回网页源代码
#print('###title ###')
print(type(soup.a.string))
