# -*- coding = utf-8 -*-
# @Time:2021/5/1919:50
# @Author:Charlie
# @File:iris_t.py
# @Software:PyCharm

import os
import types
import logging
import pdb
import sys
import functools
import unittest

import pandas as pd
import tensorflow as tf
CSV_COLUMN_NAMES = ['SepalLength','SepalWidth','PetalLength', 'PetalWidth', 'Species']
data_train = pd.read_csv('./iris_test.csv', names=CSV_COLUMN_NAMES,header=0)
data_test = pd.read_csv('./iris_training.csv', names=CSV_COLUMN_NAMES, header=0)
data_train.head()

