import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.get("file://%s/注册A.html" % base_path)
# 下拉框
alert_element = driver.find_element(By.CSS_SELECTOR, '#alerta')
confirm_element = driver.find_element(By.CSS_SELECTOR, '#confirma')
prompt_element = driver.find_element(By.CSS_SELECTOR, '#prompta ')

alert_element.click()
time.sleep(2)
alert = driver.switch_to.alert
# 确定，取消弹出框
print("alert弹框信息：",alert.text)
# alert.dismiss()
alert.accept()
time.sleep(2)
driver.quit()
