import unittest

import testcase_01

suite = unittest.TestSuite()
# suite.addTest(testcase_01.my_test('test_01'))
# suite.addTest(testcase_01.my_test('test_02'))
# 搜索指定ClassName内test开头的方法并添加
suite.addTest(unittest.makeSuite(testcase_01.my_test))

runner = unittest.TextTestRunner() #实例化
# runner.run(suite)
