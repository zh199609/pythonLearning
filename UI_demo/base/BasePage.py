from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from UI_demo.utils import UtilsDriver


class BasePage(object):
    def __init__(self):
        self.driver = UtilsDriver.get_mp_driver()
        # self.base_url = base_url
        # self.page_title = page_title

    def on_page(self, page_title):
        """
        通过title断言进入的页面是否正确
        """
        return page_title in self.driver.title

    def _open(self, url, page_title):
        """
        打开页面，并校验页面链接是否加载正确
        """
        self.driver.get(url)
        assert self.on_page(page_title)

    def open(self):
        self._open(self.base_url, self.page_title)

    def find_element(self, *location):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(location))
            return self.driver.find_element(*location)
        except:
            print(f"${self.page_title}页面未能找到${location}元素")

    def switch_frame(self, loc):
        frame_element = self.find_element(By.XPATH, loc)
        return self.driver.switch_to.frame(frame_element)

    def script(self, src):
        """
        定义script方法，用于执行js脚本，范围执行结果
        """
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            element = self.find_element(*loc)
            if click_first:
                element.click()
            if clear_first:
                element.clear()
                element.send_keys(value)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

