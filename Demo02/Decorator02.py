import time


def bar():
    time.sleep(3)
    print("in the bar")
def test(fun):
    print(fun)
    return  fun

print(test(bar))