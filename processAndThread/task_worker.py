#-*- coding = utf-8 -*-
#@Time:2021/5/1015:34
#@Author:Charlie
#@File:task_worker.py.py
#@Software:PyCharm
import os, types, logging, pdb, sys, functools, unittest

import sys, time, queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('(1)Connect to server %s ...' % server_addr)

m = QueueManager(address=(server_addr, 5000), authkey=b'abc')
m.connect()
task = m.get_task_queue()
result = m.get_result_queue()

for i in range(10):
    try:
        n = task.get(timeout=1)
        print('(2)-run task %d * %d...' % (n, n))
        r = '%d * %d = %d ' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except Queue.Empty:
        print('(3)++ task queue is empty.')
print('(4)  worker exit.')