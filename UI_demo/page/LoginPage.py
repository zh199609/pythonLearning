from selenium.webdriver.common.by import By

from UI_demo.base.BasePage import BasePage


class LoginPage(BasePage):
    username_loc = (By.NAME, 'email')
    password_loc = (By.NAME, 'password')
    submit_loc = (By.ID, 'dologin')

    def input_value(self, value, element):
        element.send_keys(value)
