import datetime
import time

print("$('.finishTime div').html('%s')" % 'xxx')
time_struct = time.strptime('2021-04-13', '%Y-%m-%d')
print(time.localtime().tm_hour)
print(time.time())

t = '2021-04-13 17:30:00'
time_struct2 = time.strptime(t, '%Y-%m-%d %H:%M:%S')
str_time = time.strftime('%Y年%m月%d日 %H时%M分%S秒', time.localtime())
print(str_time)


threeDayAgo = datetime.datetime.now() - datetime.timedelta(days=3)
print(threeDayAgo)
print(threeDayAgo.strftime('%Y-%m-%d'))
print(threeDayAgo)