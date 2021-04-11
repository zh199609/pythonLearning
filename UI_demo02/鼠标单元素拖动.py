import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file://%s/验证码/index.html" % base_path)
action = ActionChains(driver)
# 验证码拖动
element = driver.find_element(By.CSS_SELECTOR, '.handler_bg')
action.drag_and_drop_by_offset(element, 260, 0)
# 执行
action.perform()
time.sleep(1)
print(driver.find_element(By.CSS_SELECTOR, '.drag_text').text)
time.sleep(2)
driver.quit()
