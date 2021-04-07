import unittest

from parameterized import parameterized


def my_sum(a, b):
    return a + b


def setUpModule():
    print("模块级别前置处理")


def tearDownModule():
    print("模块级别前置处理")


para_list = [(1, 2, 3), (5, 6, 11), (15, 18, 33)]


class my_test(unittest.TestCase):
    def setUp(self):
        print("方法级别前置处理")

    def tearDown(self):
        print("方法级别后置处理")

    @classmethod
    def setUpClass(cls):
        print("类级别前置处理")

    @classmethod
    def tearDownClass(cls):
        print("类级别后置处理")

    # 参数化
    @parameterized.expand(para_list)
    def test_01(self, a, b, c):
        num1 = my_sum(a, b)
        self.assertEqual(num1, c)

    # 跳过
    @unittest.skip('跳过testcase')
    def test_02(self):
        self.assertEqual(my_sum(0, 100), 100)
