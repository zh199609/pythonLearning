from selenium.webdriver.common.by import By

from DataDriven.login.utils import DriverUtil


class LoginPage:
    """
    登录页面-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()
        self.username = By.ID, "username"
        self.password = By.ID, "password"
        self.verify_code = By.ID, "verify_code"
        self.login_btn = By.NAME, "sbtbutton"

    def find_username(self):
        return self.driver.find_element(*self.username)

    def find_password(self):
        return self.driver.find_element(*self.password)

    def find_verify_code(self):
        return self.driver.find_element(*self.verify_code)

    def find_login_btn(self):
        return self.driver.find_element(*self.login_btn)


class LoginHandle:
    def __init__(self):
        self.loginPage = LoginPage()

    def input_username(self, username):
        self.loginPage.find_username().send_keys(username)

    def input_password(self, pwd):
        self.loginPage.find_password().send_keys(pwd)

    def input_verify_code(self, verifyCode):
        self.loginPage.find_verify_code().send_keys(verifyCode)

    def click_login_btn(self):
        self.loginPage.find_login_btn().click()


class LoginService:
    """
    登录页面-业务层
    """

    def __init__(self):
        self.loginHandle = LoginHandle()

    def login(self, username, password, code):
        self.loginHandle.input_username(username)
        self.loginHandle.input_password(password)
        self.loginHandle.input_verify_code(code)
        self.loginHandle.click_login_btn()
