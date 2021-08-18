class Foo(object):

    def __init__(self):
        self.name = 'wupeiqi'

    def func(self):
        return 'func'


obj = Foo()

# #### 检查是否含有成员 ####
print(hasattr(obj, 'name'))
print(hasattr(obj, 'func'))
print(hasattr(obj, 'funac'))
# #### 获取成员 ####
print(getattr(obj, 'name'))
print(getattr(obj, 'func'))

# #### 设置成员 ####
setattr(obj, 'age', 18)
setattr(obj, 'show', lambda num: num + 1)

print(obj.__dict__)
print(obj.show(10))
