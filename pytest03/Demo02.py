import pytest


# 异常断言
def test_zero_division_long():
    with pytest.raises(ZeroDivisionError) as ex:
        1 / 0

    assert ex.type == ZeroDivisionError
    assert 'division by zero' in str(ex.value)


def f():
    return 3


def test_func():
    a = f()
    assert a % 2 == 0, '判断a为偶数，当前a的值为：%s' % a



