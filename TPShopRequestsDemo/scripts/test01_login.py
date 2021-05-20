import json
import os
import sys
import unittest

import requests
from nose_parameterized import parameterized

from TPShopRequestsDemo.api.login import LoginAPI




def build_data():
    test_data = []
    file = os.path.abspath('.')+'/data/loginData.json'
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


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginAPI()
        self.session = requests.Session()

    def tearDown(self):
        if self.session is not None:
            self.session.close()

    # 创建测试用例
    @parameterized.expand(build_data())
    def test01_login(self, username, password, verify_code, status_code, status, msg):
        # 调用验证码接口获取验证码，并进行断言
        response = self.login_api.get_verify_code(self.session)
        self.assertEqual(200, response.status_code)
        self.assertIn("image", response.headers.get("Content-Type"))

        # 调用登录接口获取登录信息，进行断言
        response = self.login_api.login(self.session, username, password, verify_code)
        print(response.json())
        self.assertEqual(status_code, response.status_code)
        self.assertEqual(status, response.json().get('status'))
        self.assertIn(msg, response.json().get('msg'))
