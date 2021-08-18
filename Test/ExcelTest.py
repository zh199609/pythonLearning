import pandas as pd

path = 'F:\卡中心蛋壳各单位用户信息明细.xlsx'
df = pd.read_excel(path, skiprows=2, usecols="B:H")
print(df[0:1]['部门编号（人力提供）'])
print(df[0:1]['卡中心蛋壳ID'])
