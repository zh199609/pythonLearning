# 自媒体平台的登录页面对象
import time

from selenium.webdriver.common.by import By

from uiAutoTest.base.mp.base import BasePage, BaseHandle


# 定义对象库层
class LoginPage(BasePage):
    def __init__(self):
        super(LoginPage, self).__init__()
        # 手机号码输入框
        self.mobile = By.XPATH, "//*[@placeholder='请输入手机号']"
        # 验证码输入框
        self.code = By.XPATH, "//*[@placeholder='验证码']"
        # 登录按钮
        self.login_btn = By.CSS_SELECTOR, ".el-button--primary"

    def find_mobile(self):
        return self.get_element(self.mobile)

    def find_code(self):
        return self.get_element(self.code)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 定义操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        super(LoginHandle, self).__init__()
        self.login_page = LoginPage()

    # 输入手机号码
    def input_mobile(self, text):
        self.input_text(self.login_page.find_mobile(), text)

    # 输入验证码
    def input_code(self, code):
        self.input_text(self.login_page.find_code(), code)

    # 点击登录按钮
    def click_login_btn(self):
        self.login_page.find_login_btn().click()


# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务
    def login(self, mobile, code):
        time.sleep(1)
        self.login_handle.input_mobile(mobile)
        self.login_handle.input_code(code)
        self.login_handle.click_login_btn()
