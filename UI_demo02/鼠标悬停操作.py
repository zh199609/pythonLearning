import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("file://%s/注册A.html" % base_path)
action = ActionChains(driver)
# 鼠标悬停在注册按钮上
action.move_to_element(driver.find_element(By.XPATH, '//fieldset/form/p[5]/button'))
# 执行
action.perform()
time.sleep(2)

action = ActionChains(driver)
driver.get("http://www.baidu.com")
time.sleep(1)
genduo = driver.find_element_by_link_text("更多")
action.move_to_element(genduo).perform()
time.sleep(1)
driver.find_element(By.ID,'kw').send_keys("输入内容")
time.sleep(2)
driver.quit()
