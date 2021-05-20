import time
import unittest

from requestsDemo.HTMLTestRunner import HTMLTestRunner
from requestsDemo.Test10_unitTest import TPShopLogin
from requestsDemo.Test11_unitTest_params import TPShopLogin2

suite = unittest.TestSuite()
# suite.addTest(unittest.makeSuite(TPShopLogin))
suite.addTest(unittest.makeSuite(TPShopLogin2))
report = "./report/report-{}.html".format(time.strftime("%Y-%m-%d %H-%M-%S"))
with open(report, "wb") as f:
    runner = HTMLTestRunner(f, title="TPShop登录接口测试报告")
    runner.run(suite)
    print("执行完成")
