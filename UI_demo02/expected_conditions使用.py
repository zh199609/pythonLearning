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
time.sleep(5)
driver.quit()
