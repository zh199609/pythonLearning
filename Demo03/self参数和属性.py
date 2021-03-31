class cat(object):
    def set_name(self, name):
        self.name = name

    def eat(self):
        print('%s吃' % self.name)


c = cat()
c.set_name('小花')
c.eat()
