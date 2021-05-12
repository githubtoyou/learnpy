#-*- coding = utf-8 -*-
#@Time:2021/5/418:07
#@Author:Charlie
#@File:oprationFileAndDoc.py
#@Software:PyCharm

import os, types, logging, pdb, sys, functools, unittest,shutil

# print(os.name)
# print(os.uname())
# print(os.environ)
# print(os.environ.get('ALLUSERSPROFILE'))

# print(os.path.abspath('./'))
# print(os.listdir())
# # print(os.environ.get('PATH').split(';'))
# for i in os.environ.get('PATH').split(';'):
#     if i == '':
#         break
#     print(i)
# print(os.path.join('F:\learnpy\IOprogram','ttttttttttttttttttttt'))
#os.mkdir('F:\\learnpy\\IOprogram\\ttttttttttttttttttttt')
# os.rmdir('F:\\learnpy\\IOprogram\\ttttttttttttttttttttt')
#shutil.copyfile('io.txt','io2.txt')
print(os.path.abspath('../'))
print(os.listdir('./'))
for x in os.listdir('../'):
    if os.path.isdir(x):
        print(x)
#[x for x in os.listdir('../') if os.path.isdir(x)]
print([x for x in os.listdir('./') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])



