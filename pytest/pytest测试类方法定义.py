# 定义的类名必须是以Test开头
class TestADD:
    # 定义的测试方法必须是以test开头
    def test_add(self):
        result = add(1, 2)
        print(result)
        assert result == 3

    def test_add2(self):
        result = add(3, 4)
        print(result)
        assert result == 7


def add(x, y):
    return x + y
