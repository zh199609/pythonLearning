'''
BDUSS:25SeGw2dk1JdnNuZDBXbFB5VVpkVlE5M1pyamc1VENxbzdLckwwcWpXLXJIWjFnSVFBQUFBJCQAAAAAAAAAAAEAAADtM3g-WsDatvkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKuQdWCrkHVgc

'''
import time

from selenium import webdriver

cookie = {
    'name': 'BDUSS',
    'value': '25SeGw2dk1JdnNuZDBXbFB5VVpkVlE5M1pyamc1VENxbzdLckwwcWpXLXJIWjFnSVFBQUFBJCQAAAAAAAAAAAEAAADtM3g-WsDatvkAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKuQdWCrkHVgc'
}

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
# 在浏览器中添加cookie信息
driver.add_cookie(cookie)
driver.refresh()
#页面刷新
time.sleep(3)
driver.quit()
