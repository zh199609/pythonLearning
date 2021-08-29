# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : set集合.py
# @Author  : Administrator
# @Time    : 2021-08-29 14:41:51
# @Desc    : 集合是一个无序、不重复的序列，它的基本用法包括成员检测和消除重复元素，集合对象也支持像 联合，交集，差集，对称差分等数学运算


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}

print(basket)

# 因为 set 集合只能包含不可变对象元素，而列表、集合本身都是可变对象，所以会报错
# set_ = {{1, }, {1, }}

# 创建空的集合
set = set()
# 这样就是一个字典type了
set2 = {}

# 运算符操作
# | 并集   -  补集  & 交集    ^差集

# 添加元素
basket.add('watermelon')
print(basket)

book = {
    'title': 'Python 入门基础',
    'author': '张三',
    'press': '机械工业出版社'
}
book['size'] = '100kb'
print(book)

mid = [('a', 1), ('b', 2)]

for k, v in mid:
    print(k, '-', v)

f = lambda a, b: a if a > b else b

