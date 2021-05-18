# 创建连接
import pymysql

conn = pymysql.connect(host="localhost", user='root', password='root', database='books')
# 获取游标
cursor = conn.cursor()
# 执行sql
cursor.execute('select version()')
result = cursor.fetchall()
print(result)
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
