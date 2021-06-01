import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://sahitest.com/demo/label.htm")
input1 = driver.find_elements_by_tag_name('input')[3]
input2 = driver.find_elements_by_tag_name('input')[4]
action = ActionChains(driver)
action.click(input1).perform()
input1.click()
time.sleep(1)
action.send_keys('Test Keys').perform()
time.sleep(2)
action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
time.sleep(1)
action.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
time.sleep(1)
action.key_down(Keys.CONTROL, input2).send_keys('v').key_up(Keys.CONTROL).perform()
time.sleep(2)
print(input1.get_attribute('value'))
print(input2.get_attribute('value'))
driver.quit()

'''
元素聚焦：页面直接跳到元素出现的位置
　target = driver.find_element_by_xxxx()
　　　　driver.execute_script("arguments[0].scrollIntoView();", target)
'''
