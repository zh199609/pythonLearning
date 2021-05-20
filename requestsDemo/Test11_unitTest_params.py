import json
import time

import requests
import unittest

from parameterized import parameterized


# 构造测试数据
def build_data():
    test_data = []
    file = './data/loginData.json'
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)
        for item in json_data:
            username = item.get("username")
            password = item.get("password")
            verify_code = item.get("verify_code")
            status_code = item.get("status_code")
            status = item.get("status")
            msg = item.get("msg")
            test_data.append((username, password, verify_code, status_code, status, msg))
    return test_data


class TPShopLogin2(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    def tearDown(self):
        self.session.close()

    @parameterized.expand(build_data())
    def test01_success(self, username, password, verify_code, status_code, status, msg):
        verify_response = self.session.get(url=self.verify_url)
        self.assertEqual(200, verify_response.status_code)
        self.assertIn("image", verify_response.headers.get("Content-Type"))
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        login_response = self.session.post(url=self.login_url, data=login_data)
        print(login_response.json())
        self.assertEqual(status_code, login_response.status_code)
        self.assertEqual(status, login_response.json().get('status'))
        self.assertIn(msg, login_response.json().get('msg'))
