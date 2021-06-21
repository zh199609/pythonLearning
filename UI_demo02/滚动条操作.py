import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from app import base_path

print(base_path)
driver = webdriver.Chrome()
driver.get("file://%s/注册A.html" % base_path)

# print(EC.visibility_of_element_located((By.XPATH,"//*[@id='p2']/a")))
time.sleep(2)
js = 'window.scrollTo(0,1000)'
driver.execute_script(js)
time.sleep(2)
driver.quit()
