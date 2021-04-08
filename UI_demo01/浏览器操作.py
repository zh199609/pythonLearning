import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# 窗口最大化
driver.maximize_window()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
# 设置窗口大小
# driver.set_window_size(1000,800)
# driver.set_window_position(0,0)
# 点击页面a标签  新浪
driver.find_element(By.CSS_SELECTOR, '#linkto>a').click()
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.back()
driver.find_element(By.XPATH, "//*[text()='访问 新浪 网站']").click()
time.sleep(3)
driver.close()
time.sleep(3)
driver.quit()
