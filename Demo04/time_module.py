import time

print(time.asctime())  # 返回时间格式"Fri Aug 19 11:14:16 2016",
print(time.localtime())  # 返回本地时间 的struct time对象格式

print(time.asctime(time.localtime()))
# 日期字符串 转成  时间戳
str_struct = time.strptime("2021-04-09",'%Y-%m-%d')
print(time.asctime(str_struct))
print(time.mktime(str_struct))#将str_struct时间对象转成时间戳

#将时间戳转为字符串格式
print((time.time()))
print((time.gmtime()))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()) )


