import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.support.select import Select

base_url = os.path.dirname(os.path.abspath(__file__))

driver = webdriver.Chrome()
# 访问网址
driver.get(f"file://{base_url}/select.html")

# 找到select标签元素
pro = Select(driver.find_element_by_id("pro"))

for item in pro.options:
    print(item.text)

pro.select_by_value('bj')
sleep(1)

pro.select_by_index(1)
sleep(1)

pro.select_by_visible_text('广东')
