# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : tuple.py
# @Author  : Administrator
# @Time    : 2021-08-29 14:33:55
# @Desc    : 元组

# 如果一个元组只包含一个元素
tup = (1,)
print(tup, type(tup))

tup2 = (1)
print(tup2, type(tup2))

# 元组的简写
a = 1, 2
print('a:', a, type(a))

b = (3, 4)
print('b:', b, type(b))


tup = (1,2,3,4,5)
print(tup[2])

print(1 in tup)
print(tup2.find(1))