def fun(x):
    return x + 1


def test_answer():
    assert fun(3) == 5


class TestClass:
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')

if __name__ == '__main__':
    print(hasattr('check', 'check'))