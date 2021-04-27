# -*- coding: utf-8 -*-
import os
import functools
import sys
import types

class Animal(object):
    def run(self):
        print('Animal is running ...')
# a=Animal()
#
# def fn():
#     pass
#
# print(type(fn)==types.FunctionType)
# print(type(abs)==types.BuiltinFunctionType)
# print(type(abs)==types.FunctionType)
# print(type(lambda x:x)==types.LambdaType)
# print(type((x for x in range(10)))== types.GeneratorType)

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
class Husky(Dog):

    def run(self):
        print('Husky is running...')

a = Animal()
d = Dog()
h = Husky()

class MyDog(object):
    def __len__(self):
        return 100

dog = MyDog()
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()

import sys

sys.stdout = open('stdout.log', 'a')  # 只要是file-like,不管是什么类型
print('foo')

sys.stdout = sys.__stdout__  # 恢复





