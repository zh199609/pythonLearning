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
