import time


def fun1():
    time_format = "%Y年%m月%d日 %H时%M分%S秒"
    print(time.strftime(time_format))
    print("fun1")


def fun2():
    return 0, 'hello', ['a', 'b', 'c'], {'name', 'age'}


# print(fun2())
# fun1()


def fun3(x, y):
    print("x:", x)
    print("y:", y)
    return x * y


# 默认参数
def fun4(x, y=2):
    print("x:", x)
    print("y:", y)


# 参数数组
def fun5(*x):
    print(x)


# print(fun3(y=516, x=26))

# fun4(1)


# fun5(1,23,6,'asdf')


# 这个函数就是这个变量的作用域
def fun6(name):
    print("name:", name)
    name = "修改的name"
    print("name:", name)


# 红粉 粉红  淡粉 奶白
# name = "张磊"
# fun6(name)
# print("----", name)

def calc(x):
    print(x)
    if int(x / 2) > 0:
        return calc(int(x / 2))
    print(x)
# calc(10)

# 高阶函数
def add(a,b,f):
    print(f(a))
    print(f(b))
add(-2,-9,abs)