import time

from selenium.webdriver.common.by import By

from po学习.V3.utils import UtilsDriver, get_msg


class TestLogin:

    def setup_class(self):
        self.driver = UtilsDriver.get_driver()
        self.driver.get("http://localhost/")
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".red").click()

    def teardown_class(self):
        time.sleep(2)
        UtilsDriver.quit_driver()

    # 刷新页面
    def setup(self):
        self.driver.refresh()

    def test_login_01(self):
        self.driver.find_element(By.ID, 'username').send_keys('')
        self.driver.find_element(By.ID, 'password').send_keys('15824349156')
        self.driver.find_element(By.ID, 'verify_code').send_keys('8888')
        # 点击登陆
        self.driver.find_element(By.CSS_SELECTOR, '.J-login-submit').click()
        msg = get_msg()
        print("弹框信息：", msg)
        assert "用户名不能为空" in msg

    def test_login_02(self):
        self.driver.find_element(By.ID, 'username').send_keys('15824349156')
        self.driver.find_element(By.ID, 'password').send_keys('')
        self.driver.find_element(By.ID, 'verify_code').send_keys('8888')
        # 点击登陆
        self.driver.find_element(By.CSS_SELECTOR, '.J-login-submit').click()
        pwMsg = get_msg()
        print("msg:", pwMsg)
        assert "密码不能为空" in pwMsg
