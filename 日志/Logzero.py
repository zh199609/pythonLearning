"""
logzero 日志封装
"""
import logging

import logzero as logzero


class Logzero(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.logger = logzero.logger
        # console控制台输入日志格式 - 带颜色

        self.console_format = '%(color)s ' \
                              '[%(asctime)s]-[%(levelname)1.1s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(message)s ' \
                              '%(end_color)s '
        # 创建一个Formatter对象
        self.formatter = logzero.LogFormatter(fmt=self.console_format)

        # 将formatter提供给setup_default_logger方法的formatter参数
        logzero.setup_default_logger(formatter=self.formatter)

        self.formater = logging.Formatter(
            '[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(message)s')

        logzero.loglevel(logging.DEBUG)
        logzero.logfile("./logzero.txt", formatter=self.formatter)

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def info(self, msg):
        self.logger.info(msg=msg)

    def warn(self, msg):
        self.logger.warning(msg=msg)

    def error(self, msg):
        self.logger.error(msg=msg)

    def exception(self, msg):
        self.logger.exception(msg=msg)


log_zero = Logzero()

if __name__ == '__main__':
    log_zero.debug("debug")
    log_zero.info("info")
    log_zero.warn("warn")
    log_zero.error("error")
    try:
        i = 1 / 0
    except Exception as e:
        log_zero.exception("异常了")
