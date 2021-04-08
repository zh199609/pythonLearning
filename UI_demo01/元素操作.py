import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
driver.find_element(By.ID, 'userA').send_keys("userA")
driver.find_element(By.ID, 'passwordA').send_keys('password')
driver.find_element(By.CSS_SELECTOR, '.telA').send_keys('10086')
driver.find_element(By.XPATH, "//*[@name='emailA']").send_keys("123@qq.com")
# 修改电话号码
time.sleep(3)
driver.find_element(By.ID, 'userA').clear()
driver.find_element(By.ID, 'userA').send_keys("186000000")
time.sleep(3)
driver.quit()
