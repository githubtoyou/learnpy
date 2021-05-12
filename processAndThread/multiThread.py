#coding=gbk
#-*- coding = utf-8 -*-
#@Time:2021/5/710:37
#@Author:Charlie
#@File:multiThread.py
#@Software:PyCharm

import os, types, logging, pdb, sys, functools, unittest
# import time , threading
# def loop():
#     print('(1)thread %s is running ...' % threading.current_thread().name) # 永远返回当前线程的实例
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('(2)Thread %s >>> %s ' % (threading.current_thread().name, n))
#         time.sleep(1)
#     print('--(3) thread %s ended.' % threading.current_thread().name)
#
# print('+(4) thread %s is running...' % threading.current_thread().name)# 主线程开启
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print('## (5)thread %s ended.' % threading.current_thread().name)

import time, threading, multiprocessing

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(2000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()

t1.join()
t2.join()
print(balance)
print(multiprocessing.cpu_count())



