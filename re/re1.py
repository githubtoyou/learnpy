#-*- coding = utf-8 -*-
#@Time:2021/5/1111:55
#@Author:Charlie
#@File:re1.py
#@Software:PyCharm
import os, types, logging, pdb, sys, functools, unittest
# -*- coding: utf-8 -*-
import re
# def is_valid_email(addr):
#
#     if re.match(r'[\s\w\.]+\@[\s\w]+\.[\s\w]+', addr):
#         return True
#     else:
#         return False
# # 测试:
# assert is_valid_email('someone@gmail.com')
# assert is_valid_email('bill.gates@microsoft.com')
# assert not is_valid_email('bob#example.com')
# assert not is_valid_email('mr-bob@example.com')
# print('ok')


def name_of_email(addr):
        if re.match(r'<?([\w\s]*)>?[\s]*([\w]*)@[\w]+.[\w]+',addr).group(1):
            return re.match(r'<?([\w\s]*)>?[\s]*([\w]*)@[\w]+.[\w]+',addr).group(1)
        else:
            return None


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')