param = "(%s, N'%s', N'%s', N'%s', N'%s', N'%s', N'%s'),"
with open('F:\卡中心蛋壳各单位用户信息明细.csv',encoding='utf-8') as f:
    i = 0
    for item in f:
        if (i>0):
            t = tuple(item.strip('\n').split(','))
            print(param % t)
        i = i+1