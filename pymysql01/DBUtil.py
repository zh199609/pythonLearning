import pymysql


class DBUtil():
    __conn = None
    __cursor = None

    # 创建连接
    @classmethod
    def __get_conn(cls):
        if cls.__conn is None:
            cls.__conn = pymysql.connect(host="localhost", user="root", password="root", database="books")

        return cls.__conn

    # 获取游标
    @classmethod
    def __get_cursor(cls):
        if cls.__cursor is None:
            cls.__cursor = cls.__get_cursor().cursor()
        return cls.__cursor

    # 执行sql
    @classmethod
    def exec_sql(cls, sql):
        conn = cls.__get_conn()
        cursor = cls.__get_cursor()
        try:
            pass
        except Exception as e:
            conn.rollback()
            print(e)
        finally:
            cls.__close_resource(cursor)
            cls.__close_resource(conn)

    @classmethod
    def __close_resource(cls, resource):
        if resource:
            resource.close()



if __name__ == '__main__':
    s

