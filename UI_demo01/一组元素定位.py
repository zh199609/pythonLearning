import os
import time

from selenium import webdriver

base_path = os.path.abspath('..')
driver = webdriver.Chrome()
print("file://" + base_path + "/注册A.html")
driver.get("file://" + base_path + "/pagetest/注册A.html")
'''
定位一组元素的方法:

find_elements_by_id(id)

find_elements_by_tag_name(tag_name)

定位一组元素返回的值是一个列表

可以通过下标来使用列表中的元素
'''
input_tag_list = driver.find_elements_by_tag_name('input')
for item in input_tag_list:
    print(item.location)
    if 'text'.__eq__(item.get_attribute("type")):
        item.send_keys("123456789")
time.sleep(3)
driver.quit()
