import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

base_path = os.getcwd()

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("file://%s/注册A.html" % base_path)
action = ActionChains(driver)
# 验证码拖动
userA_element = driver.find_element(By.ID, 'userA')
# 1). 输入用户名：admin1，暂停2秒，删除1
userA_element.send_keys('admin1')
time.sleep(1)
userA_element.send_keys(Keys.BACK_SPACE)  # 删除最后一个字符
# 2). 全选用户名：admin，暂停2秒
userA_element.send_keys(Keys.CONTROL, 'a')
time.sleep(1)
# 3). 复制用户名：admin，暂停2秒
userA_element.send_keys(Keys.CONTROL, 'c')
# 4). 粘贴到密码框
passwordA_element = driver.find_element(By.ID, 'passwordA')
passwordA_element.send_keys(Keys.CONTROL, 'v')
time.sleep(1)
# 执行
action.perform()
print('---------')
passwordA_element.clear()
time.sleep(2)
driver.quit()
