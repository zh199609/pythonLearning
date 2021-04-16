import time

from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
#点击百度上面的照相机按钮
driver.find_element(By.CSS_SELECTOR,'.soutu-btn').click()
# 点击选择文件
ele = driver.find_element(By.CSS_SELECTOR, ".upload-pic")
#定义鼠标对象
action = ActionChains(driver)
action.click(ele)
action.perform()
time.sleep(2)

#针对windows操作
#通过autoit来获取弹出的窗口

driver.quit()