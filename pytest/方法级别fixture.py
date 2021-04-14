import datetime


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

    def test_add_02(self):
        result = add(2, 2)
        assert result == 4
