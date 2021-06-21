import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

base_path = os.getcwd()

"""
方法	                说明
select_by_index()	通过索引定位
select_by_value() 	通过value值定位
select_by_visible_text()	通过文本值定位
deselect_all()	取消所有选项
deselect_by_index() 	取消对应index选项
deselect_by_value()  	取消对应value选项
deselect_by_visible_text() 	取消对应文本选项
first_selected_option() 	返回第一个选项
all_selected_options() 	返回所有的选项
options()	返回所以的选择项
all_selected_options()	返回所以已选中的选择项
first_selected_option()	返回选中的第一个选择项
"""


driver = webdriver.Chrome()
driver.get("file://%s/注册A.html" % base_path)
# 下拉框
time.sleep(1)
city_select = Select(driver.find_element(By.CSS_SELECTOR, '#selectA'))
city_select.select_by_index(1)
time.sleep(1)
city_select.select_by_value('gz')
time.sleep(1)
city_select.select_by_visible_text('深圳')
time.sleep(1)
# 反选，取消选择
# city_select.deselect_by_visible_text('深圳')

print("下拉框选项：")
for item in city_select.options:
    print(item.text, "---", item.get_attribute('value'))

print(city_select.first_selected_option.text)
print("所在城市: ", city_select.all_selected_options[0].text)
print("所在城市: ", city_select.all_selected_options[0].get_attribute('value'))

time.sleep(1)
driver.quit()
