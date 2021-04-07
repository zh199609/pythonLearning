try:
    a = 1 / 0
except Exception as ex:
    print("异常发生", ex)
finally:
    print("finally")
