try:
    i = 1 / 5
    print(i)
    raise Exception('主动抛出异常')
except Exception as ex:
    print("异常了",ex)
