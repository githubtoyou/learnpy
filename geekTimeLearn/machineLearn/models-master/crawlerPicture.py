# -*- coding = utf-8 -*-
# @Time:2021/5/3119:42
# @Author:Charlie
# @File:crawlerPicture.py
# @Software:PyCharm

import json
import requests
from bs4 import BeautifulSoup
import os
import shutil

url = "https://www.infoq.com/presentations/"
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Connection": "close",
    "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
    "Referer": "http://www.infoq.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
}

body = {"offset": 0, "size": 20}

def download_jpg(image_url, image_localpath):
    response = requests.get(image_url,stream = True)
    print(response)
    if response.status_code == 200:
        with open(image_localpath, 'wb') as f:
            response.raw.deconde_content = True
            shutil.copyfileobj(response.raw, f)


def craw2(url):
    response = requests.post(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    print('#########################################################################################')
    for pic_href in soup.find_all('div', class_='items__content columns'):
        # print(pic_href)
        # print('@@@@@@@@@@@@@@@@@@@@@###################')
        for pic in pic_href.find_all('img',class_='card__image'):
            #print('pic: ',pic)
            imgurl = pic.get('src')
            #print('imgurl: ',imgurl)
            dir = os.path.abspath('.')
            #print('dir: ',dir)
            filename = os.path.basename((imgurl))
            #print('filename: ',filename)
            imgpath = os.path.join(dir, filename)
            print('imgpath:',imgpath)
            #print('Start download %s' % imgurl)
            #print('@@@@@@@@@@@@@@@@@@@@@###################')
            download_jpg(imgurl, imgpath)

craw2(url)





















