# 创建连接
import pymysql

conn = pymysql.connect(host="localhost", user='root', password='root', database='books')
# 获取游标
cursor = conn.cursor()
# 执行sql
cursor.execute('select * from t_book')
print("总条数：", cursor.rowcount)
print("第一条数据:", cursor.fetchone())
print("全部查询数据：", cursor.fetchall())
# 重置游标
cursor.rownumber = 0
print(cursor.fetchall())
# 关闭游标
cursor.close()
# 关闭连接
conn.close()
