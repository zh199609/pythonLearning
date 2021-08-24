import datetime


def getNowDateTime():
    """
    获取当前日期&时间
    :return:
    """
    timestamps = str(datetime.datetime.ctime())
    return timestamps


print(getNowDateTime())
