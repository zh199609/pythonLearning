import datetime

import pytest


def add(x, y):
    return x + y


class TestAdd:
    def setup(self):
        print("前置处理", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def teardown(self):
        print("后置处理", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def test_add_01(self):
        result = add(1, 2)
        assert result == 3

    @pytest.mark.run(order=1)
    def test_add_02(self):
        result = add(2, 2)
        assert result == 4

    @pytest.mark.run(order=2)
    def test_add_03(self):
        result = add(3, 3)
        assert result == 6

    # 最后执行
    @pytest.mark.trylast
    def test_add_04(self):
        result = add(4, 4)
        assert result == 8

    def test_add_05(self):
        result = add(5, 5)
        assert result == 12

    @pytest.mark.skip("跳过测试")
    def test_add_06(self):
        result = add(5, 5)
        assert result == 12


    @pytest.mark.parametrize("x,y,expect", [(7, 7, 14), (8, 8, 16)])
    def test_add_07(self, x, y, expect):
        """

        Args:
            x ():
            y ():
            expect ():

        Returns:

        """
        result = add(x, y)
        assert result == expect
