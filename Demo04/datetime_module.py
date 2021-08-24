import datetime
# 时间加减
import time

print(time.time())
print(datetime.datetime.now())  # 2021-04-06 15:19:19.424311
print(datetime.date.fromtimestamp(time.time()))  # 时间戳直接转成日期格式 2016-08-19
print(datetime.datetime.fromtimestamp(time.time()).replace(hour=2))

print(datetime.datetime.now() + datetime.timedelta(days=3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(days=-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间-3天

c_time = datetime.datetime.now()
print(c_time.replace(minute=3, hour=2))  # 时间替换


def getTodayDate():
    """
    datetime.datetime.now().date()有相同效果
    :return:
    """
    todayDate = str(datetime.date.today())
    return todayDate

print(time.localtime().tm_year)

