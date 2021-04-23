# 定义测试类
import time

import allure
import pytest

from uiAutoTest import utils
from uiAutoTest.config import BaseDir
from uiAutoTest.page.mp.home_page import HomeProxy
from uiAutoTest.page.mp.login_page import LoginPage, LoginProxy
from uiAutoTest.page.mp.publish_page import PublishProxy
from uiAutoTest.utils import UtilsDriver, is_exist

login_case_data = utils.get_case_data(BaseDir + '/data/mp/test_login_data.json')


@pytest.mark.run(order=1)
class TestPubliseArticel:
    # 定义类级别的fixture初始化操作
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()

    # 定义类级别的fixture销毁操作
    def teardown_class(self):
        UtilsDriver.quit_mp_driver()

    # 定义登录的测试用例
    @pytest.mark.parametrize("username, code, expect", login_case_data)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, username, code, expect):
        self.login_proxy.login(username, code)
        user = self.home_proxy.get_username_msg()
        time.sleep(1)
        allure.attach(UtilsDriver.get_mp_driver().get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)
        assert user in expect

    # 定义发布文章测试方法
    @allure.severity(allure.severity_level.CRITICAL)
    def test_publish_article(self):
        # 跳转到发布文章页面
        self.home_proxy.go_publish_page()
        self.publish_proxy.publish_article("测试标题AAA", "测试内容AAA", "ios")
        assert is_exist(UtilsDriver.get_mp_driver(), '新增文章成功')
