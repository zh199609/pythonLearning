# 表示的首页面对象
from selenium.webdriver.common.by import By

from po学习.V6.base.base_page import BasePage, BaseHandle
from po学习.V6.utils import UtilsDriver


class PageHome(BasePage):
    def __init__(self):
        super().__init__()
        self.login_btn = By.CSS_SELECTOR, '.red'  #登录按钮

    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 操作层
class HandleHome(BaseHandle):
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
