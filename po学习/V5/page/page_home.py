# 表示的首页面对象
from selenium.webdriver.common.by import By

from po学习.V5.utils import UtilsDriver


class PageHome:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()
        self.login_btn = By.CSS_SELECTOR, '.red'  #登录按钮

    def find_login_btn(self):
        return self.driver.find_element(self.login_btn[0], self.login_btn[1])


# 操作层
class HandleHome:
    def __init__(self):
        self.page_home = PageHome()

    def click_login_btn(self):
        self.page_home.find_login_btn().click()


# 业务层
class HomeProxy:
    def __init__(self):
        self.handle_home = HandleHome()

    def go_login_page(self):
        self.handle_home.click_login_btn()
