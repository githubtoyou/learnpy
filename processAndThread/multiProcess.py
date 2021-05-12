#-*- coding = utf-8 -*-
#@Time:2021/5/516:48
#@Author:Charlie
#@File:multiProcess.py
#@Software:PyCharm

import os, types, logging, pdb, sys, functools, unittest
from multiprocessing import Process
from multiprocessing import Pool
import time, random, subprocess

# print('Process (%s) start ...' % os.getpid())
# pid = os.fork()
# if pid == 0 :
#     print('I am child process (%s)  and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

# def run_proc(name):
#     print('Run child process %s (%s)' % (name , os.getpid()))
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test1',))
#     print('Child process will start')
#     p.start()
#     p.join()
#     print('Child process end.')

# def long_time_task(name):
#     print('(2)--Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('(3)--Task %s runs %0.2f seconds.' % (name, (end  - start)))
#
# if __name__ == '__main__':
#     print('Parent process %s .' % os.getpid())
#     p = Pool(4)
#     print('(1)--开始执行4个子进程: ')
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('(4)--Waiting for all subprocess done ...')
#     p.close() #调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
#     p.join()    #等待所有子进程执行完毕
#     print('(5-Last)--All subprocesses done.')

# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)

# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit \n ')
# print(output.decode('GBK')) # gb2312也行，utf-8不行
# print("-------------")
# print(err.decode('GBK'))
# print('Exit code:', p.returncode)

from multiprocessing import Process,Queue
import os, time, random
def write(q):
    print('Process to write : %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

def read(q):
    print('Process to read : %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()