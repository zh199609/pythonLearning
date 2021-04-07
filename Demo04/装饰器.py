# def bar():
#     print('bar')
# def foo():
#     print('foo')
#     bar()
# foo()

#高阶函数
def bar():
    print('bar')


def test1(func):
    print(func)
    func()


test1(bar)

print("----" * 10)


def test2(func):
    print(func)
    return func


t = test2(bar)
t()  # == bar()
print('----'*10)
bar = test2(bar)
bar()

print('----'*10,'嵌套函数')

#嵌套函数

def foo2():
    print('int the foo2')
    def bar():
        print('in the bar')
    bar()
foo2()

print('----'*40)

