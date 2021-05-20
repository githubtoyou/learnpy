#-*- coding = utf-8 -*-
#@Time:2021/5/1314:21
#@Author:Charlie
#@File:hmac_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest

# import  hmac
# # message = b'Hello, world!'
# # key = b'secret'
# # h = hmac.new(key, message, digestmod = 'MD5')
# # s = h.hexdigest()
# # print(s)

# -*- coding: utf-8 -*-
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)

db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
# print(''.join([chr(random.randint(48, 122)) for i in range(20)]))
# print([chr(random.randint(48, 122)) for i in range(20)])
# print(db['michael'].username)

# def login(user, password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     if db[user] == md5.hexdigest():
#         return True
#     else:
#         return  False
def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)



# # 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')
