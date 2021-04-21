import logging.handlers
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 创建格式器
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
formatter = logging.Formatter(fmt)

# 输出到控制台
sf = logging.StreamHandler()
sf.setLevel(logging.INFO)
sf.setFormatter(formatter)
logger.addHandler(sf)

# 输出到文件
hf = logging.handlers.TimedRotatingFileHandler('log/file.txt', when='m', interval=1, backupCount=3)
hf.setLevel(logging.INFO)
hf.setFormatter(formatter)
logger.addHandler(hf)

while True:
    time.sleep(2)
    logger.info("这是一条info日志")
    logging.warning("这是一条warning日志")
