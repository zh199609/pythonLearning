import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
driver.find_element_by_tag_name('input').send_keys("admin")
# driver.find_element_by_id('passwordA').send_keys('123456')
time.sleep(3)
driver.quit()