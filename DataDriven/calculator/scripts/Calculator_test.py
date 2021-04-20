import json

import pytest

from DataDriven.calculator.page.CalculatorPage import CalculatorService
from DataDriven.calculator.utils import DriverUtil


# def build_data():
#     test_data = []
#     with open('calculator.json', encoding='UTF-8') as f:
#         test_data = json.load(f)
#     print("测试数据：", test_data)
#     return test_data
#
#
# print(build_data())


class TestCalculator:
    def setup_class(self):
        self.driver = DriverUtil.get_driver()
        self.calculatorService = CalculatorService()

    def teardown_class(self):
        DriverUtil.quit_driver()

    @pytest.mark.parametrize("a,b,expect", [(1, 1, 2), (2, 3, 5), (5, 6, 11)])
    def test_add(self, a, b, expect):
        print('a={}  b={}  expect={}'.format(a, b, expect))
        self.calculatorService.add(a, b)
        # 获取计算结果
        result = self.calculatorService.get_result()
        print("result=", result)
        assert result == str(expect)
