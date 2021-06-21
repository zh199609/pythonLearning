import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("file://%s/注册A.html" % base_path)
print("浏览器的名字：", driver.name)
print("当店页面URL:", driver.current_url)
print("获取元素坐标：", driver.find_element(By.ID, "userA").location)
# 1).获取用户名输入框的大小,返回字典  .get('height')
print(driver.find_element(By.ID, "userA").size)
# 2).获取页面上第一个超链接的文本内容
print(driver.find_element(By.LINK_TEXT, "新浪").text)
# 3).获取页面上第一个超链接的地址
print(driver.find_element(By.LINK_TEXT, "新浪").get_attribute("href"))
# 判断元素是否可见   返回值为true或者false获取元素信息.py
print(driver.find_element(By.NAME, 'sp1').is_displayed())
driver.find_element(By.ID, "userA").send_keys('\青/n春')

time.sleep(1)
driver.quit()
