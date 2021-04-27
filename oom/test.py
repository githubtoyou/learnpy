# -*- coding: utf-8 -*-
import os
import functools
import sys

# std1 = { 'name':'Michael','score':98 }
# std2 = { 'name':'Bob','score':81 }
#
# def print_score(std):
#     print('%s: %s' % (std['name'], std['score']))
#
# print_score(std2)


class Student(object):
    def  __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_score(self,score):
        if 0 <= score <= 100:
          self.__score = score
        else:
            raise ValueError('bad score !')




