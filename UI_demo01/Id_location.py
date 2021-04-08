import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
driver.find_element_by_id('userA').send_keys("admin")
driver.find_element_by_id('passwordA').send_keys('123456')
# driver.find_element(By.ID,'passwordA').send_keys('123456')
time.sleep(3)
driver.quit()