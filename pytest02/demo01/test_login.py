import time

import pytest


class TestLogin:
    age = 26

    def test_login_001(self):
        time.sleep(1)
        print("打印：test_login_001")

    @pytest.mark.skip(age > 66, reason="条件判断")
    def test_login_002(self):
        time.sleep(1)
        print("打印：test_login_002")

    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_login_003(self):
        time.sleep(1)
        print("打印：test_login_003")

    @pytest.mark.run(order=2)
    @pytest.mark.skip(reason="跳过test_login_00")
    def test_login_004(self):
        time.sleep(1)
        print("打印：test_login_004")
        assert 1 == 1

    # @pytest.mark.skip(True,reason='跳过')
    # def test_login_002(self):
    #     print("打印：test_login_002")
