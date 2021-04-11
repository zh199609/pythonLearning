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
# 在用户文本框上点击鼠标右键
action.context_click(driver.find_element(By.ID,'userA'))
#执行
action.perform()
time.sleep(3)
driver.quit()
