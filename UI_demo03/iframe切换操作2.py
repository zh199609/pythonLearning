import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.path.abspath('..') + '/pagetest'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('file://' + base_path + '/page/注册实例.html')
# 在注册实例页面中点击，注册A页面,页面条状
driver.find_element(By.ID, 'ZCA').click()
time.sleep(1.5)
# 窗口切换
print("当前窗口句柄：", driver.current_window_handle)
# 所有窗口句柄
windows = driver.window_handles
# -1 都是最后一个窗口
driver.switch_to.window(windows[-1])
# 在注册页面A中输入用户名和密码
driver.find_element(By.ID, "userA").send_keys("admin")
time.sleep(1)
driver.close()

driver.switch_to.window(windows[0])
driver.find_element(By.ID, 'ZCB').click()
time.sleep(1.5)
# 所有窗口句柄
windows = driver.window_handles
# -1 都是最后一个窗口
driver.switch_to.window(windows[-1])
driver.find_element(By.ID, "userB").send_keys("账号B")
time.sleep(2)
driver.quit()
