# 定义自媒体平台的基类
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from uiAutoTest.utils import UtilsDriver


# 对象库层基类封装
class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_mp_driver()

    def get_element(self, location):
        wait = WebDriverWait(self.driver, 10, 1)
        element = wait.until(lambda x: x.find_element(*location))
        return element


# 操作层基类封装
class BaseHandle:
    def input_text(self, element, text):
        element.send_keys(Keys.CONTROL, 'a')
        element.send_keys(Keys.DELETE)
        element.send_keys(text)
