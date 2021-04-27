# -*- coding: utf-8 -*-
import os
import functools
import sys
import types

# class Student(object):
#
#     def get_score(self):
#         return self._score
#
#     def set_score(self,value):
#         if not isinstance(value,int):
#             raise ValueError('Score must be an integer !')
#         if value < 0 or value >100:
#             raise ValueError('Score must between 0 ~ 100 !')
#         self._score = value
#
# s = Student()
# s.set_score(60)
# s.get_score()
# s.set_score(9999)

class Student(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('Score must be an integer !')
        if value < 0 or value > 100:
            raise ValueError('Score must between 0 ~ 100 !')
        self._score = value

s = Student()
s.score= 60
s.score
# s.score = 9999


class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

    @property
    def age(self):
        return 2021 - self._birth

s2 = Student2()
s2.birth = 36
print(s2.birth)
print(s2.age)

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self,value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')