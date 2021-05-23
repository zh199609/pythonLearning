import json
import unittest

from parameterized import parameterized

from IHRM import app
from IHRM.api.login import LoginAPI
from IHRM.app import BASE_DIR


def build_data():
    file_path = BASE_DIR + "/data/login.json"
    test_data = []
    with open(file_path, encoding="utf-8") as f:
        json_data = json.load(f)
        for item in json_data:
            test_data.append((item.get('login_data'), item.get("desc")))
    return test_data


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginAPI()

    def tearDown(self):
        pass

    @parameterized.expand(build_data)
    def test_login_case001(self, login_data, desc):
        print(login_data)
        print(desc)
        response = self.login_api.login(login_data);
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get('success'))
        app.TOKEN = "Bearer " + response.json().get("data")
        app.headers_data['Authorization'] = app.TOKEN
        print(app.TOKEN)
        print(app.headers_data)
