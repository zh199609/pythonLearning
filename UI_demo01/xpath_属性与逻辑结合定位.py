import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
'''
//* 或者//tag_name 开头  //*[@attribute1='value1' and @attribute2='value2']
使用属性与逻辑结合定位策略
'''
driver.find_element_by_xpath("//input[@name='user' and @class='login']").send_keys('admin')
time.sleep(3)
driver.quit()
