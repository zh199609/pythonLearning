import time

print(time.time())

local_time = time.localtime()
print(local_time.tm_year)

str_time = time.strftime('%Y-%m-%d %H:%M:%S', local_time)
print(str_time)

print(time.strptime('2021-03-25 21:05:26', '%Y-%m-%d %H:%M:%S'))
