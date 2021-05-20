# -*- coding = utf-8 -*-
# @Time:2021/5/1911:59
# @Author:Charlie
# @File:plt_t.py
# @Software:PyCharm
# Ctrl + D           复制选定的区域或行到后面或下一行
# Shift + Enter      下一行另起一行
# Ctrl + Delete      删除到字符结束--->往后删除全部
# Ctrl + Backspace    删除到字符开始《----往前删除全部
# Ctrl + /           行注释（可选中多行

import matplotlib.pyplot as plt
# plt.plot([1,3,5],[4,8,10])
# plt.show()
import numpy as np
# x = np.linspace(-np.pi,np.pi,100)
# print(x)
# plt.plot(x,np.sin(x))
# plt.show()

#曲线图
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
# plt.figure('ttt',dpi=50)
# for i in range(1,5):
#     plt.plot(x,np.sin(x/i))
# plt.show()

#生成直方图
# plt.figure(1,dpi=50)
# data = [1,1,1,1,2,2,2,3,3,4,5,5,6,5]
# plt.hist(data)
# plt.show()

#散点图
# x = np.arange(1,10)
# print(x)
# y = x
# fig = plt.figure()
# plt.scatter(x,y,c = 'r',marker='')
#
# plt.show()

import pandas as pd

# iris = pd.read_csv("./111.csv")
# print(iris.head())
# iris.plot(kind = "scatter",x = "120",y = "4")
# plt.show()

import  seaborn as sns
# import warnings
# warnings.filterwarnings("ignore")
#
iris = pd.read_csv("./iris_training.csv")
sns.set(style="white",color_codes=True)
# sns.jointplot(x="120",y="4",data=iris, size = 5)
# sns.distplot(iris['120'])
# plt.show()
#FaceGrid 一般绘图函数
#hue 彩色显示分类0/1/2
#plt.scatter 绘制散点图
#add_legend() 显示分类的描述信息
sns.FacetGrid(iris,hue="virginica",size=5).map(plt.scatter,"120","4").add_legend()
#sns.FacetGrid(iris,hue="virginica",size=5).map(plt.scatter,"setosa","versicolor").add_legend()
plt.show()


