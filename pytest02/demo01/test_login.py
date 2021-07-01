import time

import pytest


class TestLogin:

    def test_login_001(self):
        time.sleep(1)
        print("打印：test_login_001")

    def test_login_002(self):
        time.sleep(1)
        print("打印：test_login_002")

    @pytest.mark.run(order=1)
    def test_login_003(self):
        time.sleep(1)
        print("打印：test_login_003")

    @pytest.mark.run(order=2)
    def test_login_004(self):
        time.sleep(1)
        print("打印：test_login_004")
        assert 1 == 12

    # @pytest.mark.skip(True,reason='跳过')
    # def test_login_002(self):
    #     print("打印：test_login_002")
