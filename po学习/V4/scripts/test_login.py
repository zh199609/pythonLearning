# 定义测试类
import os
import sys

from po学习.V4.page.page_home import HomeProxy
from po学习.V4.page.page_login import LoginProxy
from po学习.V4.utils import UtilsDriver, get_msg

# print(__file__)
# print(os.path.abspath(__file__))
# print((os.path.dirname(os.path.abspath(__file__))))
# home_proxy = HomeProxy()

class TestLogin:
    def setup_class(self):
        # 实例化首页和登录的业务对象
        self.home_proxy = HomeProxy()
        self.login_proxy = LoginProxy()
        # 通过首页页面的业务层操作实现登录的跳转
        self.home_proxy.go_login_page()

    def setup(self):
        UtilsDriver.get_driver().refresh()

    def teardown_class(self):
        UtilsDriver.get_driver().quit()

    def test_login_01(self):
        self.login_proxy.login('15824349157', '123456', '8888')
        msg = get_msg()
        assert "账号不存在" in msg

    def test_login_02(self):
        self.login_proxy.login("15824349156","1234569","8888")
        msg = get_msg()
        assert "密码错误" in msg

    def test_login_03(self):
        self.login_proxy.login("", "1234569", "8888")
        msg = get_msg()
        assert "用户名不能为空" in msg
