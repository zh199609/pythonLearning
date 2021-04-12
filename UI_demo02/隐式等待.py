import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
# driver.maximize_window()
driver.implicitly_wait(5) #隐式等待 设置为5s
driver.get("file://%s/注册A.html" % base_path)
# 针对第一延迟框，输入admin1
driver.find_element(By.XPATH, "//*[@id='wait']/input[1]").send_keys("admin1")
# 针对第二延迟框，输入admin2
driver.find_element(By.XPATH, "//*[@id='wait']/input[2]").send_keys("admin2")

time.sleep(3)
driver.quit()
