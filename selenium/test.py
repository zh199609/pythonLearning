from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 找到搜索框
search_text = driver.find_element_by_id('kw')

# 输入搜索内容
search_text.send_keys('小菠萝测试笔记')

# 提交表单
search_text.submit()
sleep(3)
driver.quit()