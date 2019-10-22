# coding=utf-8
'''
@ Summary: 来自知乎：https://www.zhihu.com/question/28543312/answer/41208548
@ Update:  

@ file:    3-17.精简版八皇后.py
@ version: 1.0.0

@ Author:  Lebhoryi@gmail.com
@ Date:    19-10-22 下午9:05
'''

from itertools import *
cols = range(8)
for vec in permutations(cols):
    if (8 == len(set(vec[i]+i for i in cols))
          == len(set(vec[i]-i for i in cols))):
        print(vec)

