import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

base_path = os.getcwd()

driver = webdriver.Chrome()
driver.get("file://%s/注册A.html" % base_path)
# 下拉框
time.sleep(1)
city_select = Select(driver.find_element(By.CSS_SELECTOR, '#selectA'))
city_select.select_by_index(1)
time.sleep(1)
city_select.select_by_value('gz')
time.sleep(1)
city_select.select_by_visible_text('深圳')

print("所在城市: ",city_select.all_selected_options[0].text)
print("所在城市: ",city_select.all_selected_options[0].get_attribute('value'))

time.sleep(1)
driver.quit()
