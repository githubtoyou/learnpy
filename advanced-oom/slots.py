# -*- coding: utf-8 -*-
import os
import functools
import sys
import types

class Student(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99

class GraduteStudent(Student):
    pass

g = GraduteStudent()
g.score = 9999