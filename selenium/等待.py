from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# ===隐性等待20s===
# driver.implicitly_wait(20)

driver.get("http://www.baidu.com")
sleep(3)
# inputElement = driver.find_element_by_id("kw")

# 设置元素等待实例，最多等10秒，每0.5秒查看条件是否成立
element = WebDriverWait(driver, 10, 0.5).until(
    # 条件：直到元素加载完成
    EC.presence_of_element_located((By.ID, "kw"))
)

# expected_conditions最常用的类
# presence_of_element_located，检查当前DOM树种是否存在该元素（和是否可见没有关系），只要有一个元素加载出来则通过
# presence_of_all_elements_located  必须等所有匹配到的元素都加载出来才通过
