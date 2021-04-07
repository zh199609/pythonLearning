import unittest

from parameterized import parameterized

from HTMLTestRunner import HTMLTestRunner


def digital(str):
    sum = 0
    for n in str:
        if n >= '0' and n <= '9':
            sum += 1
    return sum


param_list = [('hello', 0), ('12sadf13agas', 4)]


class MyTestCast(unittest.TestCase):
    @parameterized.expand(param_list)
    def test_digital(self, a, b):
        self.assertEqual(digital(a), b)


testSuite = unittest.TestLoader().discover('./', 'practiceTest.py')
file = open('myTest.html', 'wb')
runner = HTMLTestRunner(stream=file, title="我的测试练习")
runner.run(testSuite)
