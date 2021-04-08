import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
'''
* //\**或者//tag_name       //*\*[@attribute='value']   # attribute表示的是元素的属性名，value表示的是元素对应属性值

<font color=red>如果使用class的属性进行元素定位，需要用
'''
driver.find_element_by_xpath("//*[@placeholder='请输入用户名']").send_keys('admin')
time.sleep(3)
driver.quit()
