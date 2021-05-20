#-*- coding = utf-8 -*-
#@Time:2021/5/1315:16
#@Author:Charlie
#@File:itertools_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest

import itertools, time
# natuals = itertools.count(3)
# for n in natuals:
#     time.sleep(1)
#     print(n)
# cs  = itertools.cycle('ABC')
# for c in cs:
#     time.sleep(1)
#     print(c)

# ns = itertools.repeat('A', 3)
# for n in ns:
#     print(n)
#
# natuals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 10, natuals)
# print(list(ns))

# for c in itertools.chain('ABC', 'XYZ'):
#     print(c)

# for key, group in itertools.groupby('AAABBBCCAAA'):
#     print(key, list(group))
# for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
#     print(key, list(group))


#计算圆周率可以根据公式：
#利用Python提供的itertools模块，我们来计算这个序列的前N项和：

# -*- coding: utf-8 -*-
import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...

    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.

    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    return 3.14

# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')