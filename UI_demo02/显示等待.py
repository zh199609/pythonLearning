import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

base_path = os.getcwd()

driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("file://%s/注册A.html" % base_path)
# 通过显示等待的方式定位延时输入框 输入admin
element = WebDriverWait(driver, 9, 1).until(lambda x: x.find_element(By.XPATH, "//*[@id='wait']/input[1]"))
element.send_keys("admin")



time.sleep(3)
driver.quit()
