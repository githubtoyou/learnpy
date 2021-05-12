#-*- coding = utf-8 -*-
#@Time:2021/5/119:31
#@Author:Charlie
#@File:producerConsumer.py
#@Software:PyCharm
import os, types, logging, pdb, sys, functools, unittest
from threading import Thread, current_thread
import time
import random
from queue import Queue
queue = Queue(5)

class ProducerThread(Thread):
    def run(self):
        name = current_thread().getName()
        nums = range(100)
        global queue
        while True:
            num = random.choice(nums)
            queue.put(num)
            print('(1)生产者 %s --》生产了数据 %s .' %(name, num))
            t = random.randint(1,3)
            time.sleep(t)
            print('(2)生产者%s ---》睡眠了 %s秒' %(name, t))

class ConsumerThread(Thread):
    def run(self):
        name = current_thread().getName()
        global queue
        while True:
            num = queue.get()
            queue.task_done() # 封装了线程等待和同步，类似join()
            print('(33)消费者%s--》消费了数据 %s' %(name, num))
            t = random.randint(1,5)
            time.sleep(t)
            print('(44)消费者%s ---> 休眠了%s 秒' %(name, t))

p1 = ProducerThread(name = 'threadName-->p1')
p1.start()
c1 = ConsumerThread(name = 'threadName-->c1')
c1.start()
c2 = ConsumerThread(name = 'threadName-->c2')
c2.start()

p2 = ProducerThread(name = 'threadName-->p2')
p2.start()
p3= ProducerThread(name = 'threadName-->P3')
p3.start()