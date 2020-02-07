import time


def test1():
    time.sleep(3)
    print("in the test1")


# 高阶函数
def deco(func):
    start_time = time.time()
    func()
    stop_time = time.time()
    print("deco run time %s" % (stop_time - start_time))


# deco(test1)

# 嵌套函数
def deco2(func):  # func = test2
    def deco(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print("deco run time %s" % (stop_time - start_time))

    return deco  # 返回函数内存地址


@deco2  # test2 = deco2(test2)
def test2():
    time.sleep(3)
    print("in the test2")


# timer = deco2(test2)
# timer()

test2()


@deco2
def test3(x):
    time.sleep(1)
    print("in the test3", "x:", x)


test3(111)
