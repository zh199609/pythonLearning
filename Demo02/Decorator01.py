import time

# 装饰器
'''
1.函数即变量
2.高阶函数
    a。把一个函数名当做实参传给另一个函数
    b.返回值中包含函数名
    
3.嵌套函数

高阶函数+嵌套函数=》装饰器
'''


def timmer(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        fun()
        stop_time = time.time()
        print("the timmer run time is %s" % (stop_time - start_time))

    return wrapper


@timmer
def test1():
    time.sleep(3)
    print("in the test1")


# test1()

# ---------------------------------------------------




def foo():
    print("in the foo")
    bar()
def bar():
    print("in the bar")
foo()
