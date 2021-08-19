import time
from pathlib import Path

import win32con
import win32gui
from selenium import webdriver

driver = webdriver.Chrome()
# 打开上传网站
driver.get("https://tinypng.com/")
paths = Path.cwd().parent

# 触发文件上传的操作
driver.find_element_by_css_selector("section.target").click()

time.sleep(2)
# 一级顶层窗口
dialog = win32gui.FindWindow("#32770", "打开")

# 二级窗口
comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)

# 三级窗口
comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, "ComboBox", None)

# 四级窗口 -- 文件路径输入区域
edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)

# 二级窗口 -- 打开按钮
button = win32gui.FindWindowEx(dialog, 0, "Button", None)

# 1、输入文件路径
filepath = f"{paths}\\selenium\\test.png"
win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)

# 2、点击打开按钮
win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
