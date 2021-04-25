import logging
import os
import logging.handlers

BaseDir = os.path.dirname(__file__)

#allure报告转html
# allure generate report/ -o report/html --clean

def init_loggin():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.handlers.TimedRotatingFileHandler(BaseDir + '/log/log.log', when='midnight', interval=1, backupCount=3)

    sh = logging.StreamHandler()
    fh.setLevel(logging.DEBUG)
    sh.setLevel(logging.DEBUG)

    # 创建格式器
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s"
    formatter = logging.Formatter(fmt=fmt)
    # 在处理器添加格式器
    fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(sh)

