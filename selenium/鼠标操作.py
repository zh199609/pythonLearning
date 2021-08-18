import os
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains

base_url = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()

# 创建实例
chains = ActionChains(driver)

driver.get(f"file://{base_url}/test.html")

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
login_btn = driver.find_element_by_class_name("login")
a = driver.find_element_by_id("virus-202s0")

# 悬停到指定偏移量
chains.move_to_element_with_offset(login_btn, 2, 2).perform()

sleep(5)

# 拖动1
chains.drag_and_drop(source=username, target=password)

# 拖动2
chains.drag_and_drop_by_offset(source=username, xoffset=20, yoffset=20)

# 右键点击
chains.context_click(username).perform()

# 左键点击
# chains.click(a).perform()

# 双击
chains.double_click(password).perform()

# 悬停到设置按钮
chains.move_to_element(login_btn).perform()

sleep(2)
driver.quit()

