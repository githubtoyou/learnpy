# -*- coding: utf-8 -*-
import os
import functools
import sys
import types
from enum  import Enum, unique

Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

# for name, member in Month.__members__.items():
#     print(name, '==>', member,',', member.value)

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6
day1 = Weekday.Mon

# for name, member in Weekday.__members__.items():
#     print(name, '==>', member)

class Gender(Enum):
    Male = 0
    Female = 1
    # Month = Enum('Month', ('Jan', 'Feb'))

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

