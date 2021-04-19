# 定义一个工具类
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class UtilsDriver:
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.implicitly_wait(5)
            cls._driver.get("http://localhost")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver != None:
            cls.get_driver.quit()
            cls._driver = None


def get_msg():
    time.sleep(2)
    return UtilsDriver.get_driver().find_element(By.CSS_SELECTOR, '.layui-layer-content').text
