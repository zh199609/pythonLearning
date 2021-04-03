# python中的列表生成式
'''
[变量表达式 for 变量 in 范围]
[变量表达式 for 变量 in 范围 if 条件]
[变量表达式 if 条件 else 另一个变量表达式 for 变量 in 范围]

如果if放在 for后边，则不能加else，只起到筛选作用
如果if放在for前边，可以加上else来进行两种表达式的构建
'''

print([x * 2 for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([x if x % 2 == 0 else -x for x in range(1, 11)])

'''
但是使用 ( ) 代替 [ ] 就会创建一个生成器。
一个 generator 也是一个可以迭代的对象，所以照常使用 for 循环无误，而且不需要考虑最后迭代结
'''
print([x * 2 for x in range(1, 11)])
print((x * 2 for x in range(1, 11)))
g = (x for x in range(5))
for i in g:
    print(i, end="  ")

'''
只要包含 yield 关键字的函数就是一个 generator ，yield 的作用是中断函数的运行并且返回后边的值，
这也就完成了一次 generator 的迭代/更新，也就是说调用一次 next函数，就会使得 generator 继续执行，
直到遇到下一个 yield 就再次中断，返回后边的值。
'''
print("使用yield创建迭代器")


def odd():
    print("step1:")
    yield 1
    print("step2")
    yield 2
    print("step3")
    yield 3
    return


odd = odd()
# print(next(odd))
# print(next(odd))
# print(next(odd))
# print(next(odd))
for i in odd:
    print(i)
'''
所以其实使用函数来定义 generator 给定义更复杂的生成器更新规则提供了可能，
但是注意使用函数定义的 generator 必须要有可以结束的条件，否则生成器会一直更新下去。

但是有一个问题就是，如果最后一个 yield 后边还有其他代码，那就无法执行，但是可以通过异常处理来完成：
'''
