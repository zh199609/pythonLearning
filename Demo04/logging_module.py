import logging

logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")

logging.basicConfig(filename='./example.log',level=logging.INFO)
logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warn message")