try:
    i = 1 / 1
    j = int('6')
except ZeroDivisionError:
    print("除数不能为零")
except ValueError:
    print("数值转换错误")
except:
    print('出现异常了')
else:
    print("没有异常")
