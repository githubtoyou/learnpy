#-*- coding = utf-8 -*-
#@Time:2021/5/1313:29
#@Author:Charlie
#@File:hashlib_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest
# import hashlib
# md5 = hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
#
# md51 = hashlib.md5()
# md51.update('how to use md5 in python hashlib??'.encode('utf-8'))
# print(md51.hexdigest())

# -*- coding: utf-8 -*-
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
import hashlib
def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if db[user] == md5.hexdigest():
        return True
    else:
        return  False

# user = 'michael'
# password = '123456'
# print(db[user])
# md5 = hashlib.md5()
# md5.update(password.encode('utf-8'))
# print(md5.hexdigest())
# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
