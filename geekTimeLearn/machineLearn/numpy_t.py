#-*- coding = utf-8 -*-
#@Time:2021/5/1811:32
#@Author:Charlie
#@File:numpy_t.py
#@Software:PyCharm
#Ctrl + D           复制选定的区域或行到后面或下一行
#Shift + Enter      下一行另起一行
#Ctrl + Delete      删除到字符结束--->往后删除全部
#Ctrl + Backspace    删除到字符开始《----往前删除全部
#Ctrl + /           行注释（可选中多行
import os, types, logging, pdb, sys, functools, unittest
import numpy as np
# arr1 = np.array([2,3,4])
# # print(arr1)
# # print(arr1.dtype)
# arr2 = np.array([1.2,2.3,3.4])
# # print(arr2.dtype)
# # print(arr1+arr2)
#
# # print(arr2 * 10)
#
# data = [[1,2,3],[4,5,6]]
# arr3 = np.array(data)
# print(arr3)
# print(arr3.dtype)

# print(np.zeros((3,5)))
# print(np.ones((4, 6)))

#print(np.empty((2,3,2)))
arr4 = np.arange(10)
print(arr4[5:8])

print(list(range(10)))

