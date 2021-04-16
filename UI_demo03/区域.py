import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://172.16.208.78:20006/RegionalMarketing/closePlanDetail/74299')
driver.find_element(By.ID, 'security_username').send_keys("1")
driver.find_element(By.ID, 'security_password').send_keys("1")
driver.find_element(By.ID, 'submit').click()
# driver.find_element(By.XPATH, "//*[@class='newPlan']/span[2]/a").click()
# driver.find_element(By.NAME, 'planName').send_keys('方案名称1')
# driver.find_element(By.NAME, 'applicantTel').send_keys('10086')
# driver.find_element(By.XPATH,"//*[@for='reportType']").click()


print(driver.get_cookies())
print(driver.get_cookie('JSESSIONID').get('value'))
data_js = "$('.finishTime div').html('%s')"

print(driver.find_element(By.XPATH,"//span[text()='活动类型：']").text)
print(driver.find_element(By.XPATH,"//span[text()='活动类型：']/following-sibling::span[1]").text)
time.sleep(3)
driver.quit()
