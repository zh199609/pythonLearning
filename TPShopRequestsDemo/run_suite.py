import time
import unittest

from TPShopRequestsDemo.scripts.test01_login import TestLogin
from TPShopRequestsDemo.tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(TestLogin))
report = "./report/report-{}.html".format(time.strftime("%Y-%m-%d %H-%M-%S"))

with open(report, "wb") as f:
    runner = HTMLTestRunner(f, title="TPShop接口测测试报告")
    runner.run(suite)
    print("执行完成")
