# 创建连接
import pymysql

conn = pymysql.connect(host="localhost", user='root', password='root', database='books', autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行sql
sql = "update t_book set title = '西游记修改01' where id = 4"
cursor.execute(sql)
print("影响的记录数：", cursor.rowcount)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()

try:
    print('try')
except Exception as e:
    print(e)
finally:
    print('finally')
