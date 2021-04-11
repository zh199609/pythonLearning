import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file://%s/注册A.html" % base_path)
action = ActionChains(driver)
userA_element = driver.find_element(By.ID, 'userA')
userA_element.send_keys("admin")
time.sleep(1)
# 双击选中
action.double_click(userA_element)
# 执行
action.perform()
time.sleep(3)
driver.quit()
