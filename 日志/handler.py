import logging.handlers
import time

logger = logging.getLogger("myLogger")  # 创建logger日志器
logger.setLevel(logging.DEBUG)  # 设置日志器的级别

# 按时间来切割   每隔5秒
handler = logging.handlers.TimedRotatingFileHandler('log/test.txt', when='s', interval=5)
handler.setLevel(logging.INFO)
# 将处理器添加到日志器
logger.addHandler(handler)

#  输出日志信息
logger.info("这是一条info信息级别的日志!")
time.sleep(6)
logger.info("这是一条info信息级别的日志!")
