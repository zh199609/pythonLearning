import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.get("file://%s/注册A.html" % base_path)
time.sleep(2)
js = 'window.scrollTo(0,1000)'
driver.execute_script(js)
time.sleep(2)
driver.quit()
