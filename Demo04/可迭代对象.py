# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 可迭代对象.py
# @Author  : Administrator
# @Time    : 2021-08-28 16:02:13
# @Desc    : 可迭代对象

"""
答案就是实现__iter__()方法，只要一个对象定义了__iter__()方法，那么它就是可迭代对象。Iterable


如果一个对象同时实现了__iter__()和__next()__()方法，那么它就是迭代器。Iterator

通过for循环对一个可迭代对象进行迭代时，for循环内部机制会自动通过调用iter()方法执行可迭代对象内部定义的__iter__()方法来获取一个迭代器，
然后一次又一次得迭代过程中通过调用next()方法执行迭代器内部定义的__next__()方法获取下一个元素，当没有下一个元素时，
for循环自动捕获并处理StopIteration异常。如果你还没明白，请看下面用while循环实现for循环功能，整个过程、原理都是一样的：

（1）生成器是一种特殊的迭代器，拥有迭代器的所有特性；

（2）迭代器使用return返回值而生成器使用yield返回值每一次对生成器执行next()都会在yield处暂停；

（3）迭代器和生成器虽然都执行next()方法时返回下一个元素，迭代器在实例化前就已知所有元素，但是采用惰性计算机制，共有多少元素，下一个元素是什么都是未知的，每一次对生成器对象执行next()方法才会产生下一个元素。


"""
from collections import Iterable

from tqdm import tqdm


class A():
    def __iter__(self):
        print("iter^")


print('A是可迭代对象吗：', isinstance(A(), Iterable))


# 生成器 是特殊的迭代器
def fun_gen():
    index = 1
    while index < 100000000:
        if index % 2 == 0:
            yield index
        index += 1


g = fun_gen()

print(next(g))
for i in range(1, 10):
    print(next(g))

# 生成器解析式：      ：(返回值 for 元素 in 可迭代对象 if 条件)
g2 = (i * 10 for i in range(10) if i % 2 == 0)
print("生成器表达式：", g2)
for i in g2:
    print(i)

# 列表生成式，双重循环
res = ['*'.join([str(i), str(j)]) for i in range(10) for j in range(10)]
print("列表生成式，双重循环：", res)

# 列表解析式
li = [i for i in range(10) if i % 2 == 0]
print(li)

d = {'a': '1', 'b': '2'}
for k, v in d.items():
    print(k, ':', v)
print(isinstance(d.items(), enumerate))


# 斐波拉契数列
def fib(max):
    print('斐波拉契数列：')
    n, a, b = 0, 0, 1
    while (n < max):
        print(b)
        a, b = b, a + b
        n += 1


fib(8)


# 使用生成器
def fib_gen(max):
    n, a, b = 0, 0, 1
    while (n < max):
        yield b
        a, b = b, a + b
        n += 1


fg = fib_gen(8)
print("使用生成器生成：")
print(next(fg))
print(next(fg))
print(next(fg))
print(next(fg))

a = []
#在 Python 长循环中添加一个进度提示信息，用户只需要封装任意的迭代器 tqdm(iterator)。
for i in tqdm(range(1000)):
    temp = ['你好'] * 2000
    a.append(temp)
