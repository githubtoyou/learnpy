# -*- coding: utf-8 -*-
import os
import functools
import sys
import types

class Hello(object):
    def hello(self, name = 'world'):
        print('Hello, %s .' % name )


