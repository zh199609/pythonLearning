import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.path.abspath('..') + '/pagetest'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('file://' + base_path + '/注册实例.html')

# 针对 主页输入
driver.find_element(By.ID, 'userA').send_keys('admin1')
# 针对注册用户A iframe 输入
driver.switch_to.frame(driver.find_element(By.ID, 'idframe1'))
driver.find_element(By.ID, 'AuserA').send_keys('AuserA')
# 切换回主页，才能切换到其他iframe
driver.switch_to.default_content()
# 切换
driver.switch_to.frame(driver.find_element(By.ID, 'idframe2'))
driver.find_element(By.ID, 'BuserA').send_keys('BuserA')
time.sleep(2)
driver.quit()
