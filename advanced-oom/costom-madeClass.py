# -*- coding: utf-8 -*-
import os
import functools
import sys
import types

class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):  #定制类：只要定义好__str__()方法，就可以返回一个好看的字符串；
        return 'Student object (name:%s)' % self.name
    __repr__ = __str__

## __iter__ 该方法返回一个迭代对象

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1
    def __iter__(self):
        return self
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a
# for n in Fib():
#     print(n)


# for n in Fib()[5]:
#     print(n)

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
# print(Fib2()[10])
# print(Fib2()[0:5])

class Student2(object):
    def __init__(self):
        self.name = 'Michaels'
    # def __getattr__(self, attr):
    #     if attr=='score':
    #         return  99
    # def __getattr__(self, attr):
    #     elif attr == 'age':
    #         return lambda: 25
    def __getattr__(self, attr):
        if attr == 'agg':
            return lambda: 250000
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

class Chain(object):
    def __init__(self, path = ''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s%s' % (self._path, path))
    def __str__(self):
        return self._path
    __repr__ = __str__

# print(Chain().status.user.timeline.list)
# Chain().status.user.timeline.list

class Student3(object):
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print('My name is %s .' % self.name)

# s = Student3('Michael')
# s()
# t=callable(Student3)
# print(t)

