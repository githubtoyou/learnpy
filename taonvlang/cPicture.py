#-*- coding = utf-8 -*-
#@Time:2021/5/3120:08
#@Author:Charlie
#@File:cPicture.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import json
import requests
from bs4 import BeautifulSoup
import os
import shutil
from taonvlang import str_to_json

url = "https://www.infoq.com/presentations/"
head = '''
:authority: cdn.infoq.com
:method: GET
:path: /statics_s2_20210511-0409/scripts/infoq.js
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7
cookie: _ga=GA1.2.1132852512.1621499687; __gads=ID=83f2aed988632f79:T=1621499688:S=ALNI_MaNiKDUbtonov8QDnzngjMmSI4rTw; infoq_survey=4FFA012AA56B5CF424E1F31D95C237AB|7; _gid=GA1.2.533813946.1622454211; _fbp=fb.1.1622454293192.1533265480
if-modified-since: Wed, 28 Apr 2021 10:05:34 GMT
referer: https://www.infoq.com/presentations/
sec-ch-ua: " Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"
sec-ch-ua-mobile: ?0
sec-fetch-dest: script
sec-fetch-mode: no-cors
sec-fetch-site: same-site
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36
'''
print(str_to_json.strToJson(head))

