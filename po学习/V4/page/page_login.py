# 表示的登录页面对象
from selenium.webdriver.common.by import By

from po学习.V4.utils import UtilsDriver

#对象库层
class LoginPage:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()

    def find_username(self):
        return self.driver.find_element(By.ID, 'username')

    def find_password(self):
        return self.driver.find_element(By.ID, "password")

    def find_code(self):
        return self.driver.find_element(By.ID, "verify_code")

    # 登陆按钮
    def find_login(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".J-login-submit")


# 操作层
class LoginHandle:
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        self.login_page.find_username().send_keys(username)

    def input_password(self, password):
        self.login_page.find_password().send_keys(password)

    def input_code(self, code):
        self.login_page.find_code().send_keys(code)

    def click_login(self):
        self.login_page.find_login().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.driver = LoginHandle()

    def login(self, username, password, code):
        self.driver.input_username(username)
        self.driver.input_password(password)
        self.driver.input_code(code)
        self.driver.click_login()
