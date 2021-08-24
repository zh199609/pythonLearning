import logging
from logging import handlers


class Loggers:
    """
    logging日志封装
    """
    __instance = None
    """
    __new__至少要有一个参数cls，代表要实例化的类，此参数在实例化时由Python解释器自动提供

__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类__new__出来的实例，或者直接是object的__new__出来的实例

__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值
    """

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        formater = logging.Formatter(
            '[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(funcName)s:%(lineno)d] : %(message)s')

        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        # 输出文件
        self.fileLogger = handlers.RotatingFileHandler('./test.txt', maxBytes=5242880, backupCount=3)

        # 输出控制台
        self.consoleLogger = logging.StreamHandler()
        self.consoleLogger.setLevel(logging.DEBUG)

        self.fileLogger.setFormatter(formater)
        self.consoleLogger.setFormatter(formater)

        self.logger.addHandler(self.fileLogger)
        self.logger.addHandler(self.consoleLogger)

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def info(self, msg):
        self.logger.info(msg=msg)

    def warn(self, msg):
        self.logger.warning(msg=msg)

    def error(self, msg):
        self.logger.error(msg=msg)

    def exception(self, msg):
        self.exception(msg=msg)


loggers = Loggers()

if __name__ == '__main__':
    loggers.info("我是 Loggers INFO")
    loggers.debug("我是 Loggers debug")
    loggers.warn("我是 Loggers warn")
    loggers.error("我是 Loggers error")
    # loggers.exception("我是 Loggers exception")
