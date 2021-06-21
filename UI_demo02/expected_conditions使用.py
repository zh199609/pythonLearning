import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/index/")
print('开始', time.ctime())
# <input id="toStation" type="hidden" value="" name="to_station">
# 这个元素默认是隐藏的
toStationEl = driver.find_element(By.ID,'toStation')
print(toStationEl.is_displayed())
print(EC.visibility_of(toStationEl)(driver))
time.sleep(1)
# <input type="text" class="input error" value="" id="toStationText">
#这个元素是可见的
print(EC.visibility_of(driver.find_element(By.ID,'toStationText'))(driver))
print(EC.visibility_of(driver.find_element(By.ID,'toStationText'))(driver).tag_name)

driver.quit()
