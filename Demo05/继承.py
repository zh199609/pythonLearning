# class People: 经典写法
class People(object):  # 新式类写法
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print('%s:在吃东西' % self.name)

    def sleep(self):
        print('%s:在睡觉' % self.name)


class Relation(object):

    def make_friends(self, obj):
        print("%s交朋友%s" % (self.name, obj.name))


#         继承People
class Man(People, Relation):
    def __init__(self, name, age, param):
        # super().__init__(name, age)
        super(Man, self).__init__(name, age)  # 新式类写法
        self.param = param

    def eat(self):
        print('%s:在抽烟' % self.name)

    def show(self):
        print(self.name, self.age, self.param)


m1 = Man("男人一号", '26', "我是男人")
m2 = Man("男人二号", '26', "我是男人")
m1.eat()
m1.sleep()
m1.show()
m1.make_friends(m2)

print("--------"*5)


class Woman(People):
    def get_birth(self):
        print("%s：在生孩子" % self.name)


w1 = Woman("女人一号", '25')
w1.get_birth()
