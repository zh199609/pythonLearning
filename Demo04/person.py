# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : person.py
# @Author  : Administrator
# @Time    : 2021-08-26 17:19:35
# @Desc    : 类方法，静态方法

class Person:
    name = "cppl man"

    def self_m(self):
        self.name = "self.name"
        print(Person.name)
        print(self.name)


p = Person()

p.self_m()
print(Person.name)
