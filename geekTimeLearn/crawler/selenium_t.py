#-*- coding = utf-8 -*-
#@Time:2021/6/320:15
#@Author:Charlie
#@File:selenium.py
#@Software:PyCharm
#打开浏览器，2打开网址，3点击密码，4定位账号密码，5输入内容，6点击登录豆瓣
from selenium import webdriver
import time

#driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get('https://accounts.douban.com/passport/login')
#driver.get('https://www.douban.com')

driver.find_element_by_class_name('account-tab-account').click()

driver.find_element_by_id('username').send_keys('111')
time.sleep(2)
driver.find_element_by_id('password').send_keys('111')
time.sleep(2)
driver.find_element_by_link_text('登录豆瓣').click()
# time.sleep(3)
# html = driver.page_source
# print(html)
# time.sleep(3)
# driver.quit()