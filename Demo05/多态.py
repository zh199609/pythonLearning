class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError('子类必须实现该方法')

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Cat(Animal):

    def talk(self):
        print('Meow')


class Dog(Animal):
    def talk(self):
        print('汪汪')


d1 = Dog('小黄')
d1.talk()
m1 = Cat('小猫')
m1.talk()

Animal.animal_talk(d1)

print(10 / 4)

dict = {'name': 'xx'}
for item in dict.items():
    key, value = item
    print(key, value)
