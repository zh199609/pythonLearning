# 创建连接
import pymysql

conn = pymysql.connect(host="localhost", user='root', password='root', database='books', autocommit=True)
# 获取游标
cursor = conn.cursor()
# 执行sql
sql = "insert into t_book(id, title, pub_date) values(5, '西游记', '2021-01- 01');"
cursor.execute(sql)
print("影响的记录数：", cursor.rowcount)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
