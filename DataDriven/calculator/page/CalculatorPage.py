import time

from selenium.webdriver.common.by import By

from DataDriven.calculator.utils import DriverUtil


class CalculatorPage:
    """
    计算器页面-对象库层
    """

    def __init__(self):
        self.driver = DriverUtil.get_driver()
        # 数字按钮
        self.digit_btn = By.ID, "simple{}"
        self.add_btn = By.ID, "simpleAdd"
        self.equal_btn = By.ID, "simpleEqual"
        self.result_btn = By.ID, "resultIpt"

    def find_digit_btn(self, digit):
        location = self.digit_btn[0], self.digit_btn[1].format(digit)
        return self.driver.find_element(*location)

    def find_add_btn(self):
        return self.driver.find_element(*self.add_btn)

    def find_equal_btn(self):
        return self.driver.find_element(*self.equal_btn)

    def find_result_btn(self):
        return self.driver.find_element(*self.result_btn)


class CalculatorHandle:
    """
    计算器页面-操作层
    """

    def __init__(self):
        self.calculatorPage = CalculatorPage()

    def click_digit_btn(self, digit):
        self.calculatorPage.find_digit_btn(digit).click()

    def click_add_btn(self):
        self.calculatorPage.find_add_btn().click()

    def click_eq_btn(self):
        self.calculatorPage.find_equal_btn().click()

    def get_result(self):
        return self.calculatorPage.find_result_btn().get_attribute("value")


class CalculatorService:
    """
    计算器页面-业务层
    """

    def __init__(self):
        self.calculatorHandle = CalculatorHandle()

    def add(self, num1, num2):
        self.calculatorHandle.click_digit_btn(num1)
        self.calculatorHandle.click_add_btn()
        self.calculatorHandle.click_digit_btn(num2)
        self.calculatorHandle.click_eq_btn()

    def get_result(self):
        time.sleep(1)
        return self.calculatorHandle.get_result()
