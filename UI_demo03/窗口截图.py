import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.path.abspath('..') + '/pagetest'
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('file://' + base_path + '/page/注册实例.html')
try:
    driver.find_element(By.ID, 'userA').send_keys('userA')
except  Exception as e:
    print(e)
    # 如果存在目录，需要提前手动创建
    driver.get_screenshot_as_file('img/error.png')
    driver.close()
    raise e
time.sleep(2)
driver.quit()
