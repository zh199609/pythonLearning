import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://localhost/")
# 先登录
driver.find_element(By.XPATH, "//*[@class='fl nologin']/a[1]").click()
# 输入用户密码
driver.find_element(By.ID, 'username').send_keys("15824349156")
driver.find_element(By.ID, 'password').send_keys("123456")
driver.find_element(By.ID, 'verify_code').send_keys("8888")
driver.find_element(By.CSS_SELECTOR, '.J-login-submit').click()


time.sleep(10)
# 购物车数量
print('---')
print("购物车商品数量：", driver.find_element(By.ID, "cart_quantity").text)

time.sleep(3)
driver.quit()
