import time


class TestLogin:
    age = 26

    def test_login_001(self):
        time.sleep(1)
        print("打印：test_login_001")

    def test_login_002(self, user_fixture):
        time.sleep(1)
        print("打印：test_login_002")
