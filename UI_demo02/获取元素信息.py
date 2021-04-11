import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file://%s/注册A.html" % base_path)
# 1).获取用户名输入框的大小,返回字典  .get('height')
print(driver.find_element(By.ID, "userA").size)
# 2).获取页面上第一个超链接的文本内容
print(driver.find_element(By.LINK_TEXT, "新浪").text)
# 3).获取页面上第一个超链接的地址
print(driver.find_element(By.LINK_TEXT, "新浪").get_attribute("href"))
# 判断元素是否可见   返回值为true或者false获取元素信息.py
print(driver.find_element(By.NAME,'sp1').is_displayed())
# time.sleep(3)
driver.quit()
