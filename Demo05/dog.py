class Dog:
    n = 3  # 类变量

    def __init__(self, name):
        self.name = name  # 实例变量

    def bulk(self):
        print("%s:狗叫" % self.name)


d1 = Dog("小黑")
d1.bulk()
d2 = Dog("小白")
d2.bulk()
