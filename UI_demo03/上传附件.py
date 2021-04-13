import time

import autoit
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")
driver.find_element(By.CSS_SELECTOR, '.soutu-btn').click()
ele = driver.find_element(By.CSS_SELECTOR, '.upload-pic')
# 点击选择文件  使用鼠标操作
action = ActionChains(driver)
action.click(ele)
action.perform()
time.sleep(2)
# 针对windows操作
# 通过autoit来获取弹出的窗口
autoit.win_wait_active('打开', 3)
# 在文件选择输入框中输入文件的地址及文件名称
autoit.control_send('打开', 'Edit1', r'C:\Users\alan\Desktop\印章(已去底).jpg')
# 在弹出窗口中点击打开按钮
autoit.control_click('打开', 'Button1')
time.sleep(7)
driver.quit()
