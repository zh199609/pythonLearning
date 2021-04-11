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
# 鼠标悬停在注册按钮上
action.move_to_element(driver.find_element(By.XPATH, '//fieldset/form/p[5]/button'))
# 执行
action.perform()
time.sleep(3)
driver.quit()
