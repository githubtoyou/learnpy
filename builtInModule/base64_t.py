#-*- coding = utf-8 -*-
#@Time:2021/5/1220:07
#@Author:Charlie
#@File:base64_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest

# import base64
# b1 = base64.b64encode(b'binary\x00string')
# print(b1)
# b2 = base64.b64decode(b'YmluYXIAc3RyaW5n')
# print(b2)
# b3 = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(b3)
# b4 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
# print(b4)
# b5 = base64.urlsafe_b64decode('abcd--__')
# print(b5)

#请写一个能处理去掉=的base64解码函数：

# -*- coding: utf-8 -*-
import base64
def safe_base64_decode(s):
    while len(s) < 8:
        s+='='
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode('YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode('YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

# b1 = safe_base64_decode('YWJjZA')
# print(b1)

# s = 'YWJjZA'
# while len(s) < 8:
#     # return len(s)
#     s+='='
#     print(s)
# ss= safe_base64_decode('YWJjZA==')
# print(ss)
