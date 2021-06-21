import os
import time
import unittest

from IHRM.scripts.TestEmployee import TestEmployee
from IHRM.scripts.test01_login import TestLogin
from IHRM.tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestEmployee))
report = os.getcwd() + "/report/report-{}.html".format(time.strftime("%Y-%m-%d %H-%M-%S"))
with open(report, 'wb') as f:
    runner = HTMLTestRunner(f, title="IHRM登录报告")
    runner.run(suite)
