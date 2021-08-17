from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.baidu.com")

print(f'标签页：{driver.title}')
print(f'标签页url:{driver.current_url}')
print(f'标签页name：{driver.name}')
# print(f"标签页page_source：{driver.page_source}")

# 获取当前标签页句柄
print(driver.current_window_handle)

# 打开新的标签页
js = 'window.open("https://www.baidu.com/")'
driver.execute_script(js)

driver.get("https://www.jd.com")

# 获取当前标签页句柄
print(driver.current_window_handle)

# 获取浏览器所有标签页句柄
handles = driver.window_handles
print(handles)

driver.switch_to.window(handles[1])
print(driver.current_window_handle)
# # 关闭当前标签页
# driver.close()

sleep(5)


driver.quit()