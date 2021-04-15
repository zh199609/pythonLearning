import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class UtilsDriver:
    _driver = None

    # 类级别的方法
    @classmethod
    def get_driver(cls):
        #判断driver是否创建
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.implicitly_wait(7)
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None

# 定义一个弹出框消息获取方法
def get_msg(driver):
    time.sleep(1)
    driver = UtilsDriver.get_driver()
    return driver.find_element(By.CSS_SELECTOR, '.layui-layer-content').text
