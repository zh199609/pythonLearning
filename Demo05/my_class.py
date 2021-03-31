class my_calss(object):
    index = 0

    def __init__(self):
        my_calss.index += 1

    # 类方法
    @classmethod
    def count(cls):
        my_calss.index += 1
        print(cls.index)

    @staticmethod
    def show_help():
        my_calss.index += 1
        print("静态方法", my_calss.index)


a = my_calss()
a.index=5
b = my_calss()
c = my_calss()
my_calss.count()
my_calss.count()
my_calss.show_help()
