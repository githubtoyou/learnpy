#-*- coding = utf-8 -*-
#@Time:2021/6/313:43
#@Author:Charlie
#@File:test.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest
import dbdb

price9 = 9
price2 = 2
z9 = 0.9
z6 = 0.6

days  = 22
TFtime = 15

totals1 = 0
totals2 = 0

totals1 = ( price9 * TFtime * z9 ) + price9 * ( days - TFtime ) * z6
print(totals1)

totals2 = ( price2 * ( TFtime -0) * z9 ) + price9 * ( days + 0 )  * z6
print(totals2)

t = totals2  -totals1
print(t)


