import os
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url = os.path.dirname(os.path.abspath(__file__))
driver = webdriver.Chrome()

# 访问网址
driver.get("https://www.baidu.com")

# 找到搜索框
inputElement = driver.find_element_by_id("kw")

# 输入搜索内容
inputElement.send_keys("内容")

# ctrl+a全选
inputElement.send_keys(Keys.CONTROL, "a")

sleep(1)

inputElement.send_keys(Keys.CONTROL, 'x')
sleep(1)

inputElement.clear()

sleep(1)

inputElement.send_keys(Keys.CONTROL, 'v')
sleep(1)
# 删除键
inputElement.send_keys(Keys.BACKSPACE)
sleep(1)

# tab
inputElement.send_keys(Keys.TAB)
sleep(1)

# 回车键
inputElement.send_keys(Keys.ENTER)
sleep(1)

sleep(1)

driver.quit()


