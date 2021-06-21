import requests


class LoginAPI:
    def __init__(self):
        self.url = "http://ihrm-test.itheima.net/api/sys/login"
        pass

    def login(self, login_data):
        return requests.post(self.url, json=login_data)
