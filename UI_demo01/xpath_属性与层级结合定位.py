import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file://D:/BaiduNetdiskDownload/02讲义 笔记 软件/09、UI自动化测试及黑马头条项目实战/UI自动化/UI自动化/web自动化工具集合/pagetest/注册A.html")
'''
是以//*或者//tag_name开头    //p[@id='pa']/input

在任意层给当中，都可以结合属性来使用
使用层级与属性结合定位策略
'''
driver.find_element_by_xpath("//p[@id='p1']/input").send_keys('使用层级与属性结合定位策略')
time.sleep(3)
driver.quit()

'''
//*[text() = 'value']   value表示的是要定位的元素的全部文本内容.   

//*[contains(@attribute,'value')]   attribute表示的属性名称, value表示的是字符串

  要定位的元素中，att‘’‘ribute属性的属性值包含了value的内容。

//*[starts-with(@attribute,'value')]      attribute表示的属性名称, value表示的是字符串

  要定位的元素，attribute属性的属性值是以value开头

'''
