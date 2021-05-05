#-*- coding = utf-8 -*-
#@Time:2021/5/414:32
#@Author:Charlie
#@File:docTest.py
#@Software:PyCharm

import os, types, logging, pdb, sys, functools, unittest,re

m = re.search('(?<=abc)def', 'abcdef')
print(m.group(0))


def abs(n):
    '''
    Function to get absolute value of number.
    Example:
    >>>abs(1)
    >>>abs(-1)
    >>>abs(0)
    :param n:
    :return:
    '''
    return n if n >=0 else (-n)
p = re.compile('ca*t')
print(p.match('caaaaat'))