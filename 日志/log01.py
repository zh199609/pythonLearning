import logging

logging.basicConfig(filename="log/log.txt",
                    format="[%(levelname)s]  %(filename)s  %(lineno)d  %(asctime)s --%(message)s", level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")

try:
    c = 1 / 0
except Exception as e:
    logging.error(e)
    logging.exception("Exception occurred")
