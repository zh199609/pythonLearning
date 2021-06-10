# 构建测试数据
import json
import time

from DataDriven.login import utils
from DataDriven.login.page.LoginPage import LoginService
from DataDriven.login.utils import DriverUtil


def build_data():
    json_data = []
    with open('../login.json', encoding="utf-8") as f:
        test_data = json.load(f)
    for item in test_data:
        json_data.append((item.get("username"),
                          item.get("password"),
                          item.get("code"),
                          item.get("is_success"),
                          item.get("expect")))
    return json_data


class TestLogin:
    def setup_class(self):
        self.driver = DriverUtil.get_driver()
        self.loginService = LoginService()

    def teardown_class(self):
        DriverUtil.quit_driver()

    def setup(self):
        # 进入首页
        self.driver.get("http:localhost")
        # 点击登录链接
        self.driver.find_element_by_link_text("登录").click()

    def test_login(self, username, password, code, is_success, expect):
        self.loginService.login(username, password, code)
        time.sleep(1)
        # 登录成功
        if is_success:
            time.sleep(1)
            assert expect in self.driver.title
        else:
            msg = utils.get_tips_msg()
            assert expect in msg
