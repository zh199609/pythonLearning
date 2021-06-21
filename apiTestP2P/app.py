import logging
import os
from logging import handlers

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_URL = "http://user-p2p-test.itheima.net"


def init_logging_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    sh = logging.StreamHandler()

    log_path = BASE_DIR + os.sep + 'log' + os.sep + 'p2p.log'

    fh = logging.handlers.TimedRotatingFileHandler(log_path, when="M", interval=1, backupCount=7,
                                                   encoding="UTF-8")

    f = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(f)

    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(sh)
    logger.addHandler(fh)
