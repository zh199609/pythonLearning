import os
from time import sleep

from selenium import webdriver

base_url = os.path.dirname(os.path.abspath(__file__))

print()
driver = webdriver.Chrome()
# 访问网址
driver.get(f"file://{base_url}/test.html")

# 找到id = username的元素
username = driver.find_element_by_id("username")

# 输入值 张三
username.send_keys("张三")
sleep(2)
# 清空内容
username.clear()

login_btn = driver.find_element_by_class_name("login")
# 打印 元素宽高
print(f"元素宽高:{login_btn.size}")
# 打印 元素 x , y坐标值
print(f"元素坐标值：{login_btn.location}")
# 点击
login_btn.click()

# 获取第一个标签为a的文本
a_text = driver.find_element_by_tag_name("a")
print("获取a标签文本：", a_text.text)

# 获取第一个标签为div的文本
div_text = driver.find_element_by_tag_name("div")
print("获取div标签文本:", div_text.text)

# 获取元素属性值
a_attr = driver.find_element_by_class_name("mnav")
print("获取元素属性值：", a_attr.get_attribute("href"))


# 找到 不可见元素
ant_btn3 = driver.find_element_by_class_name("ant-btn3")
# 找到 可见元素
ant_btn4 = driver.find_element_by_class_name("ant-btn4")

# 查看是否可见
print("不可见元素:", ant_btn3.is_displayed())
print("可见元素:", ant_btn4.is_displayed())


# 找到 不可点击元素
ant_btn3 = driver.find_element_by_class_name("ant-btn1")
# 找到 可点击元素
ant_btn4 = driver.find_element_by_class_name("ant-btn2")

# 查看是否可点击
print("不可点击元素:", ant_btn3.is_enabled())
print("可点击元素:", ant_btn4.is_enabled())

# 找到 未被选中的元素
option1 = driver.find_elements_by_tag_name("option")[0]
# 找到 已被选中的元素
option2 = driver.find_elements_by_tag_name("option")[-1]

# 查看是否被选择
print("未被选择元素:", option1.is_selected())
print("已被选择元素:", option2.is_selected())


sleep(3)
driver.quit()
