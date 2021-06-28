import time
import unittest

from apiTestP2P.app import BASE_DIR
from apiTestP2P.lib.HTMLTestRunner import HTMLTestRunner
from apiTestP2P.script.login import login

suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))

report = BASE_DIR + '/report/report{}.html'.format(time.strftime('%Y-%m-%d %H-%M-%S'))
with open(report, 'wb') as f:
    runner = HTMLTestRunner(f, title='P2P金融项目接口测试报告', description='测试开发')
    runner.run(suite)
