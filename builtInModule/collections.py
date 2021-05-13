#-*- coding = utf-8 -*-
#@Time:2021/5/1214:18
#@Author:Charlie
#@File:collections.py
#@Software:PyCharm
import os, types, logging, pdb, sys, functools, unittest
# from collections import namedtuple
# Point = namedtuple('Point1', ['x', 'y'])
# p = Point(1, 2)
# print(p.x)
# print(p.y)
# print(isinstance(p, Point))

# from collections import deque
# q = deque(['a', 'b','c'])
# q.append('x')
# q.appendleft('y')
# print(q[1])

# from collections import defaultdict
# dd = defaultdict(lambda: 'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

# from collections import OrderedDict
# d = dict([('a', 1),('b', 2),('c', 3), ('d', 4)])
# print(d)

# from collections import ChainMap
# import os, argparse
# # 构造缺省参数:
# defaults = {
#     'color': 'red',
#     'user': 'guest'
# }
# # 构造命令行参数:
# # #创建一个解析器——创建 ArgumentParser() 对象
# parser = argparse.ArgumentParser()
# # #添加参数——调用 add_argument() 方法添加参数
# parser.add_argument('-u', '--user')
# parser.add_argument('-c', '--color')
# # #解析参数——使用 parse_args() 解析添加的参数
# namespace = parser.parse_args()
# #创建一个字典，存放字典类型的数据：
# command_line_args = { k: v for k, v in vars(namespace).items() if v }
# # for k,v in vars(namespace).items():
# #     if v:
# #         print(k,v)
# combined = ChainMap(command_line_args, os.environ, defaults)
# print(command_line_args)
# # print('color=%s' % combined['color'])
# # print('user=%s' % combined['user'])
# # print(vars(namespace).items())
# # print(vars(namespace))


# import argparse
# #创建一个解析器——创建 ArgumentParser() 对象
# parser = argparse.ArgumentParser(description='test',usage='test2')
# #添加参数——调用 add_argument() 方法添加参数
# parser.add_argument('--sparse', action='store_true', default=False, help='GAT with sparse version or not.')
# parser.add_argument('--seed', type=int, default=72, help='Random seed.')
# parser.add_argument('--epochs', type=int, default=10000, help='Number of epochs to train.')
# #解析参数——使用 parse_args() 解析添加的参数
# args = parser.parse_args()
# print(args.sparse)
# print(args.seed)
# print(args.epochs)
#
# print(parser,args)

import time
from collections import Counter
c =  Counter()
for ch in 'programming':
    print(ch, c[ch])
#    time.sleep(1)
    c[ch] = c[ch] + 1
    print('----',ch, c[ch])
#    time.sleep(1)
print(c)
c.update('hello')
print(c)
