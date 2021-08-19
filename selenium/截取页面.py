from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

# 截取整个页面
driver.get_screenshot_as_file("test.png")
driver.save_screenshot("tests.png")

# 找到搜索框
inputElement = driver.find_element_by_id("kw")

# 截取搜索框元素
inputElement.screenshot("inputElement.png")
