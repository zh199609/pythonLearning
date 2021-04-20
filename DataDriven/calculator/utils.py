from selenium import webdriver


class DriverUtil:
    """
    浏览器驱动工具类
    """
    _driver = None

    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()
            cls._driver.implicitly_wait(10)
            cls._driver.get("http://cal.apple886.com/")
        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._driver is not None:
            cls._driver.quit()
            cls._driver = None
