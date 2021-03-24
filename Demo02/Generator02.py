from time import sleep

def consumer(name):
    print("%s 准备吃包子啦！" % name)
    while True:
        baozi = yield
        print("包子【%s】来了，被【%s】吃了！" % (baozi, name))
c =consumer("张磊")
c.__next__()
# c.__next__()
c.send("肉包子")