import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from time import sleep

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()

driver.get('http://sahitest.com/demo/label.htm')

input1 = driver.find_elements_by_tag_name('input')[3]
input2 = driver.find_elements_by_tag_name('input')[4]

# ----------复制-----------
action = ActionChains(driver)
input1.click()
action.click(input1).perform()
action.send_keys('Test Keys')
time.sleep(1)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL)  # ctrl+a
time.sleep(1)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL)  # ctrl+c
time.sleep(1)
action.key_down(Keys.CONTROL, input2).send_keys('v').key_up(Keys.CONTROL).perform()  # ctrl+v
time.sleep(1)

# "--------复制 -----------"
# input1.send_keys('Test Keys')
# time.sleep(1)
# input1.send_keys(Keys.CONTROL, 'a')
# time.sleep(1)
# print(input1.send_keys(Keys.CONTROL, 'c'))
# print(input1)
# time.sleep(1)
# input2.send_keys(Keys.CONTROL, 'v')
# time.sleep(1)

# -----结果-------
print(input1.get_attribute('value'))
print(input2.get_attribute('value'))
driver.quit()

'''
元素聚焦：页面直接跳到元素出现的位置
　target = driver.find_element_by_xxxx()
　　　　driver.execute_script("arguments[0].scrollIntoView();", target)
'''
