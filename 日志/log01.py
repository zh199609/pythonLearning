import logging

logging.basicConfig(filename="log/log.txt",
                    format="[%(levelname)s]  %(filename)s  %(lineno)d  %(asctime)s --%(message)s", level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
