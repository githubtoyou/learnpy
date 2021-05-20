# -*- coding = utf-8 -*-
# @Time:2021/5/416:39
# @Author:Charlie
# @File:fileReadAndWrite.py
# @Software:PyCharm

import os
import types
import logging
import pdb
import sys
import functools
import unittest
# try:
#     f = open('F:\learnpy\IOprogram\io.txt', 'r')
#     ff = f.read()
#     print(ff)
# finally:
#     if f:
#         f.close()

# with open('F:\learnpy\IOprogram\io.txt', 'r') as f:
#     for line in f.readlines():
#         print(line.strip())

# with open(r'F:\learnpy\IOprogram\t.jpg', 'rb') as f:
#     for line in f.readlines():
#         print(line.strip())

# f = open(r'F:\learnpy\IOprogram\t.jpg', 'rb')
# print(f.read())
import time
with open('F:\\learnpy\\IOprogram\\io.txt', 'a') as f:
    f.write('\n测试!')

with open('F:\\learnpy\\IOprogram\\io.txt', 'r') as f:
    print(f.read())
