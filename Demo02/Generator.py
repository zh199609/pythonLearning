# 迭代器&生成器
'''
生成器只有在调用时才生成相应的数据

'''
a = [i * 2 for i in range(10)]
print(a)

# 生成器   只记住当前位置
# __next()__方法 获取下一个
b = (i * 2 for i in range(10))
print(b)
print(next(b))
print(b.__next__())
print(b.__next__())
# for i in b:
#     print(i)


# 用函数做生成器
print('-------------------------')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        '''
            相当于
            t = (b,a+b) t是一个tuple
            a = t[0]
            b = t[1]
        '''
        n = n + 1
    return 'done'


fib_gen = fib(10)
print(fib_gen)
for i in fib_gen:
    print(i)
#交换值
x = 3
y = 7
x = x + y
y = x - y
x = x - y
print(x)
print(y)
