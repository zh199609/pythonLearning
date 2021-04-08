import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
'''
定位一组元素的方法:

find_elements_by_id(id)

find_elements_by_tag_name(tag_name)

定位一组元素返回的值是一个列表

可以通过下标来使用列表中的元素
'''
input_tag_list = driver.find_elements_by_tag_name('input')
for item in input_tag_list:
    if 'text'.__eq__(item.get_attribute("type")):
        item.send_keys("123456789")
time.sleep(3)
driver.quit()
