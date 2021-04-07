import time


def test1():
    time.sleep(1)
    print('test1')


def test2():
    time.sleep(2)
    print('test2')


def deco(func):
    start = time.time()
    return func
    end = time.time()
    print('this func run time: %s' % (end - start))


test1 = deco(test1)
test1()

print('-----------')


def deco2(func):
    def deco_inner(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('this func run time: %s' % (end - start))
        return res

    return deco_inner


test2 = deco2(test2)
test2()  # --> deco_inner()

print('----' * 10, '装饰器=高阶函数+嵌套函数')


# 语法糖 = test3 = deco2(test3)
@deco2
def test3():
    time.sleep(3)
    print('test3')


test3()


@deco2  # test4 = deco2(test4)
def test4(name):
    print('test4', name)
    time.sleep(1)


test4('参数')


@deco2
def test5(age):
    print('test5', age)
    return age


print("返回值：", test5(77))
