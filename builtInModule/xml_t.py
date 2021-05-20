#-*- coding = utf-8 -*-
#@Time:2021/5/1414:39
#@Author:Charlie
#@File:xml_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest

# from xml.parsers.expat import ParserCreate
#
# class DefaultSaxHandler(object):
#     def start_element(self, name, attrs):
#         print('(1)sax:start_element: %s, attrs: %s' % (name, str(attrs)))
#
#     def end_element(self, name):
#         print('(2)sax:end_element: %s' % name)
#
#     def char_data(self, text):
#         print('(3)sax:char_data: %s' % text)
#
# xml = r'''<?xml version="1.0"?>
# <ol>
#     <li><a href="/python">Python</a></li>
#     <li><a href="/ruby">Ruby</a></li>
# </ol>
# '''
#
# handler = DefaultSaxHandler()
# parser = ParserCreate()
# parser.StartElementHandler = handler.start_element
# parser.EndElementHandler = handler.end_element
# parser.CharacterDataHandler = handler.char_data
# parser.Parse(xml)

L= []
L.append(r'<?xml version="1.0"?>')
L.append(r'<root>')
#L.append(encode('some & data'))
L.append(r'<root>')
#return ''.join(L)
print(L)
