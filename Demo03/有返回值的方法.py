class cat:
    def __init__(self, name='tom'):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    # 直接打印对象，可调用此方法
    def __str__(self):
        return self.name


c1 = cat('小猫')
c1.set_name("笑话")
print(c1.get_name())
print(c1)
