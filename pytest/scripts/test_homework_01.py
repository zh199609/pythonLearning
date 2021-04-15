import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("http://localhost/")
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, ".red").click()

    def teardown_class(self):
        time.sleep(2)
        self.driver.quit()

    # 刷新页面
    def setup(self):
        self.driver.refresh()

    def test_login_01(self):
        self.driver.find_element(By.ID, 'username').send_keys('')
        self.driver.find_element(By.ID, 'password').send_keys('15824349156')
        self.driver.find_element(By.ID, 'verify_code').send_keys('8888')
        # 点击登陆
        self.driver.find_element(By.CSS_SELECTOR, '.J-login-submit').click()
        time.sleep(1)
        msg = self.driver.find_element(By.CSS_SELECTOR, '.layui-layer-content').text
        print("弹框信息：", msg)
        assert "用户名不能为空" in msg

    def test_login_02(self):
        self.driver.find_element(By.ID, 'username').send_keys('15824349156')
        self.driver.find_element(By.ID, 'password').send_keys('')
        self.driver.find_element(By.ID, 'verify_code').send_keys('8888')
        # 点击登陆
        self.driver.find_element(By.CSS_SELECTOR, '.J-login-submit').click()
        time.sleep(1)
        pwMsg = self.driver.find_element(By.CSS_SELECTOR, '.layui-layer-content').text
        print("msg:", pwMsg)
        assert "密码不能为空" in pwMsg
