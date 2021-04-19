# 定义一个对象库层基类
from selenium.webdriver.support.wait import WebDriverWait

from po学习.V6.utils import UtilsDriver


class BasePage:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    def get_element(self, location):
        element = WebDriverWait(self.driver, 10, 1).until(lambda x: x.find_element(*location))
        return element


# 定一个操作层的基类
class BaseHandle:
    # 定义元素输入操作方法
    def input_text(self, elemet, text):
        elemet.clear()
        elemet.send_keys(text)
