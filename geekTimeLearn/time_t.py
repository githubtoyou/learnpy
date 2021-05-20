# -*- coding = utf-8 -*-
# @Time:2021/5/1810:11
# @Author:Charlie
# @File:time_t.py
# @Software:PyCharm
# Ctrl + D           复制选定的区域或行到后面或下一行
# Shift + Enter      下一行另起一行
# Ctrl + Delete      删除到字符结束--->往后删除全部
# Ctrl + Backspace    删除到字符开始《----往前删除全部
# Ctrl + /           行注释（可选中多行
import datetime
import os
import types
import logging
import pdb
import sys
import functools
import unittest
import time
# print(time.time())
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))
# print(datetime.datetime.now())
# print(datetime.timedelta(minutes=10))
# print(datetime.datetime.now() + datetime.timedelta(minutes=10))
# one_day = datetime.datetime(2008, 5, 27)
# new_date = datetime.timedelta(days=10)
# print(one_day + new_date)

# import  random
# print(random.randint(1,5))
# print(random.choice(['aa','bb','cc']))

import os
# print(os.path.abspath('..'))
# print(os.path.exists('/user'))
# print(os.path.isdir('F:\learnpy'))
# print(os.path.join('/tmp/a/','b/c'))

from pathlib import Path
# p = Path('.')
# print(p.resolve())
q = Path('F:\\learnpy\\geekTimeLearn\\a\\b\\c')
Path.mkdir(q, parents=True)
