import time

import requests
import unittest
from HTMLTestRunner import HTMLTestRunner


class TPShopLogin(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        self.session.close()

    def test01_success(self):
        verify_response = self.session.get(url=self.verify_url)
        self.assertEqual(200, verify_response.status_code)
        self.assertIn("image", verify_response.headers.get("Content-Type"))
        login_data = {
            "username": "15824349156",
            "password": "123456",
            "verify_code": "8888"
        }
        login_response = self.session.post(url=self.login_url, data=login_data)
        print(login_response.json())
        self.assertEqual(200, login_response.status_code)
        self.assertEqual(1, login_response.json().get('status'))
        self.assertIn("登陆成功", login_response.json().get('msg'))

    # 账号不存在
    def test02_user_is_notExist(self):
        verify_response = self.session.get(url=self.verify_url)
        self.assertEqual(200, verify_response.status_code)
        self.assertIn("image", verify_response.headers.get("Content-Type"))
        # 发登录请求并断言
        login_data = {
            "username": "13488888899",
            "password": "123456",
            "verify_code": "8888"
        }
        login_response = self.session.post(url=self.login_url, data=login_data)
        print(login_response.json())
        self.assertEqual(200, login_response.status_code)
        self.assertEqual(-1, login_response.json().get("status"))
        self.assertIn("账号不存在", login_response.json().get("msg"))



