import time

from selenium import webdriver
driver = webdriver.Chrome()#创建谷歌浏览器驱动对象
# webdriver.Firefox()
# webdriver.Edge()
# webdriver.Ie()

driver.get("http://www.baidu.com")

time.sleep(3)  #快捷导包方式

driver.quit()

