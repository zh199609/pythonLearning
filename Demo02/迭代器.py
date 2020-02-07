from typing import Iterable, Iterator

list = [1, 2, "fds"]
# 判断是否是迭代对象
# 可用被next()函数调用并不断返回下一个值的对象称为迭代器Iterator
# 生成器都是Iterator对象，但list，dict，str虽然是Iterable 却不是Iterator
# 把list，dict，str等Iterable变成Iterator可以使用iter()函数
print(isinstance(list, Iterable))

a = [564, "a"]
b = iter(a)
print(isinstance(b, Iterator))
print(b.__next__())
print(b.__next__())
