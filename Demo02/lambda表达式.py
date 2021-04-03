# funcName = lambda parameters : expression
from functools import reduce
from typing import Iterable, Iterator

add = lambda x, y: x + y
print(add)
print(add(0, 1))

# zip,zip(*),map,reduce,filter

'''
zip() 函数接受（零个）、一个、多个可迭代对象（iterable）为参数，将这些 iterable 合并成一个tuple，返回一个对象，可以使用 list 将返回的 zip 对象转换成列表，列表的长度是所有传入的 iterable 对象中可迭代最短的个数
zip(*) 是 zip 的逆过程，可以将一个 zip 对象返回成多个 iterable 对象，返回的结果依然可以使用 list 转换成列表
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [10, 12, 30]
zip1 = zip(a, b)
print(zip1)
ss = list(zip1)
print(ss)

zip2 = zip(a, b, c)
print(list(zip2))
print('分割符'.center(10, '-'))
a1, b1 = zip(*ss)
print(a1)

'''
map 函数接受两个参数，一个是一个函数，另一个是一个可迭代对象（iterable），
map将该函数依次作用给可迭代对象中的每一个元素，然后返回的结果再封装成一个迭代器（iterator）
'''
print(isinstance(a, Iterable))
print(isinstance(iter(a), Iterator))


def f(x):
    return x ** 2


s = map(f, range(10))
ss = list(s)
for item in s:
    print(item,end=',')
print("====="*5)
for item in ss:
    print(item,end=',')
for item in ss:
    print(item,end=',')
print()
print("分割符".center(10,'-'))

'''
reduce 接受的参数和 map 一样，不同的作用是 reduce 是依次根据传入的可迭代对象的每个元素，
然后把每一次的结果跟下一个元素进行计算
'''
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
#比如一个很经典的结合 map 和 reduce 一起使用的例子是将一个纯数字的 string 变成 int 值：
def f(x,y):
    return x*10 + y

def g(c):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[c]

a = reduce(f,map(g,'13579'))
print(a)
print(type(a))
'''
filter 函数和 map 类似，但是 filter 是根据所接收的那个函数的返回结果是 True 还是 False 来筛选传入的那个可迭代对象中的元素，
如果该函数作用在一个元素上时返回的是 True，那么这个元素也会出现在返回的结果中，反之就不会被返回：
'''