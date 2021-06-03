# -*- coding = utf-8 -*-
# @Time:2021/5/2615:12
# @Author:Charlie
# @File:spider.py
# @Software:PyCharm
# Ctrl + D           复制选定的区域或行到后面或下一行
# Shift + Enter      下一行另起一行
# Ctrl + Delete      删除到字符结束--->往后删除全部
# Ctrl + Backspace    删除到字符开始《----往前删除全部
# Ctrl + /           行注释（可选中多行
import requests
from json import loads

#淘女郎-模特url地址
#url = 'https://www.infoq.cn/public/v1/article/get_news_list'
#url = 'https://v.taobao.com/v/content/live?catetype=704&from=taonvlang'
url = 'https://v.taobao.com/micromission/req/selectCreatorV3.do?cateType=704&&_output_charset=UTF-8&_input_charset=UTF-8&_csrf=c63662e7-fe5c-4cae-9c6f-c86f272f2827'
# data = {
#     'size': 20,
#     'offset': 0
# }
def getTitleList():
    response = requests.post(url)
    # html = response.json()
    print(response)
    # result = loads(html)
    # return result['data ']['data ']['result ']

getTitleList()
# for user in getTitleList():
#     print(user)