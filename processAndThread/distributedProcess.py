#-*- coding = utf-8 -*-
#@Time:2021/5/1011:43
#@Author:Charlie
#@File:distributedProcess.py
#@Software:PyCharm
# import os, types, logging, pdb, sys, functools, unittest
# import random, time, queue
# from multiprocessing.managers import BaseManager
# task_queue = queue.Queue()
# result_queue = queue.Queue()
# class QueueManager(BaseManager):
#     pass
# QueueManager.register('get_task_queue', callable=lambda: task_queue)
# QueueManager.register('get_resule_queue', callable=lambda : result_queue)
#
# manager = QueueManager(address=('', 5000), authkey=b'abc')
# manager.start()
# task = manager.get_task_queue()
# result = manager.get_result_queue()
#
# for i in range(10):
#     r = result.get(timeout=10)
#     print('Result : %s ' % r)
#
# manager.shutdown()
# print('Master exit .')


import random, time, queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = queue.Queue()
# 接收结果的队列:
result_queue = queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('', 5000), authkey=b'abc')
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('(1)--Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('(2)--Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('(3)--Result: %s' % r)
# 关闭:
manager.shutdown()
print('(4)--master exit.')