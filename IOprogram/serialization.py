#-*- coding = utf-8 -*-
#@Time:2021/5/514:24
#@Author:Charlie
#@File:serialization.py
#@Software:PyCharm

import os, types, logging, pdb, sys, functools, unittest,pickle,json

# d = dict(name = 'Bob', age = 20, score = 88)
# p = pickle.dumps(d)
# print(p)
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()
#
# ff = open('dump.txt', 'rb')
# dd = pickle.load(ff)
# ff.close()
# print(d)

# with open('dump.txt','r') as f:
#     print(f.read())

# json.dumps(d)
# print(d)
# json_str = '{"age":20, "score":88, "name": "Bob"}'
# j = json.loads(json_str)
# print(j)

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
# s = Student('Bob', 20 , 88)
# def student2dict(std):
#     return{
#         'name':std.name,
#         'age':std.age,
#         'score':std.score
#     }
# # print(json.dumps(s, default= student2dict))
# print(json.dumps(s, default=lambda obj: obj.__dict__))

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))
