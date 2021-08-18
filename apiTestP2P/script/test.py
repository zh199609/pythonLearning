class Dog(object):
    """我是注释 """
    name = '我是名称'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        print('is esting')

    @classmethod
    def zoo(cls):
        print('zoo', cls.name)

    def __call__(self, *args, **kwargs):
        print("我是call")


if __name__ == '__main__':
    d = Dog('哈士奇')
    # print(d.name)
    # d.eat()
    # d.zoo()

    print(Dog.__doc__)
    print('当前操作的对象在那个模块：', Dog.__module__)
    print('标识当前操作的对象的类是什么：', Dog.__class__)
    d()


class Province:
    country = "shanghai"

    def __init__(self, name, count):
        self.name = name
        self.count = count

    def func(self, *args, **kwargs):
        print("func")


if __name__ == '__main__':
    print(Province.__dict__)
    obj1 = Province('嘉兴', '1000')
    print(obj1.__dict__)


class Foo:
    def __getitem__(self, item):
        print('__getitem__', item)

    def __setitem__(self, key, value):
        print('__setitem__', key, value)

    def __delitem__(self, key):
        print('__delitem__', key)


if __name__ == '__main__':
    obj = Foo()
    result = obj['k1']  # 自动触发执行 __getitem__
    obj['k1'] = '我是值'  # 自动触发执行 __getitem__
