import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
'''
相对路径  匹配任意层级的元素，是以 //tag_name或者//* 开头

也可以使用下标，下标是从1开始。

例子：//p[5]/button

'''
driver.find_element_by_xpath('//form/p[2]/input').send_keys('123456')
time.sleep(3)
driver.quit()
