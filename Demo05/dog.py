class Dog:
    n = 3  # 类变量
    name = '实例变量name'

    def __init__(self, name, life):
        self.name = name  # 实例变量
        self.__life = life  # 私有属性

    def bulk(self):
        print("%s:狗叫" % self.name)

    #     析构函数   调用del xx 会执行该函数
    def __del__(self):
        print("del")

    def show_life(self):
        self.__private_fun()
        return self.__life

    def __private_fun(self):
        print("私有方法")


d1 = Dog("小黑", "d1")
d1.bulk()
d1.name = '实例name'  # 给实例添加了一个name属性，不影响类变量
# 先找实例变量，在变类变量
print(d1.name)
print(d1.n)
print("私有属性：", d1.show_life())
del d1
d2 = Dog("小白", 'd2')
d2.bulk()
