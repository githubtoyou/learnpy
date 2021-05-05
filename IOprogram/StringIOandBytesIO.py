#-*- coding = utf-8 -*-
#@Time:2021/5/417:55
#@Author:Charlie
#@File:StringIOandBytesIO.py
#@Software:PyCharm

import os, types, logging, pdb, sys, functools, unittest,io
from  io import StringIO
# f = StringIO()
# print(f.write('hello'))
# print(f.write(' '))
# print(f.write('world!'))
# print(f.getvalue())

# f = StringIO('Hello! \nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())

from io import BytesIO
# f = BytesIO()
# f.write('中文'.encode('utf-8'))
# print(f.write('中文'.encode('utf-8')))
# print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87\xe4\xb8\xad\xe6\x96\x87')
print(f.read())
