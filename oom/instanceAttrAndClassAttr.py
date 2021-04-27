# -*- coding: utf-8 -*-
import os
import functools
import sys
import types


class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count += 1

if Student.count != 0:
    print('测试失败1!')
    print(Student.count)
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('测试失败2!')
        print(Student.count)
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('测试失败3!')
            print(Student.count)
        else:
            print('Students:', Student.count)
            print('测试通过!')
            print(Student.count)