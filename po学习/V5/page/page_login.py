# 表示的登录页面对象
from selenium.webdriver.common.by import By

# 对象库层
from po学习.V5.utils import UtilsDriver


class LoginPage:
    def __init__(self):
        self.driver = UtilsDriver.get_driver()
        self.username = By.ID, 'username'  # 用户名输入框
        self.password = By.ID, "password"
        self.code = By.ID, "verify_code"
        self.loginBtn = By.CSS_SELECTOR, ".J-login-submit"

    def find_username(self):
        return self.driver.find_element(*self.username)

    def find_password(self):
        return self.driver.find_element(*self.password)

    def find_code(self):
        return self.driver.find_element(*self.code)

    # 登陆按钮
    def find_login(self):
        return self.driver.find_element(*self.loginBtn)


# 操作层
class LoginHandle:
    def __init__(self):
        self.login_page = LoginPage()

    def input_username(self, username):
        element = self.login_page.find_username()
        element.clear()
        element.send_keys(username)

    def input_password(self, password):
        element = self.login_page.find_password()
        element.clear()
        element.send_keys(password)

    def input_code(self, code):
        element = self.login_page.find_code()
        element.clear()
        element.send_keys(code)

    def click_login(self):
        element = self.login_page.find_login()
        element.clear()
        element.click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.driver = LoginHandle()

    def login(self, username, password, code):
        self.driver.input_username(username)
        self.driver.input_password(password)
        self.driver.input_code(code)
        self.driver.click_login()
