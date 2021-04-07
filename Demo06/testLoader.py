import unittest

from HTMLTestRunner import HTMLTestRunner

suite = unittest.TestLoader().discover('./', 'my*.py')

# ruuner = unittest.TextTestRunner()
# 使用wb代表用二进制写方式打开，不用写encoding
file = open('test01.html', 'wb')
ruuner = HTMLTestRunner(stream=file, title='我的第一个html测试报告')
ruuner.run(suite)
file.close()
