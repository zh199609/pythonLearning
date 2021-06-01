import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()
"""
# 浏览器弹出框：
#（1）使用switch_to方法先切换到浏览器弹出框
    # driver.switch_to.alert
#（2）Alert类提供了一系列的操作方法
    # dismiss(): 否
    # accept(): 是
    # text(): 获取弹出框里的内容
    # Send_keys(): 在弹出框里输入文本
"""
driver = webdriver.Chrome()
driver.get("file://%s/注册A.html" % base_path)
# 下拉框
alert_element = driver.find_element(By.CSS_SELECTOR, '#alerta')
confirm_element = driver.find_element(By.CSS_SELECTOR, '#confirma')
prompt_element = driver.find_element(By.CSS_SELECTOR, '#prompta')

# 点击 跳出alert弹框
alert_element.click()
time.sleep(2)
alert = driver.switch_to.alert
# 确定，取消弹出框
print("alert弹框信息：", alert.text)
# alert.dismiss()
alert.accept()
time.sleep(2)


confirm_element.click()


driver.quit()
