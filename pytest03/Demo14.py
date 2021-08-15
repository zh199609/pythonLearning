import pytest

"""
第二行即使断言失败，后面的断言还是会继续执行
"""
# def test_add1():
#     assert 1 + 4 == 5
#     assert 1 + 3 == 3
#     assert 2 + 5 == 7
#     assert 2 + 5 == 9
#     print("测试完成")


def test_add2():
    pytest.assume(1 + 4 == 5)
    pytest.assume(1 + 3 == 3)
    pytest.assume(2 + 5 == 7)
    pytest.assume(2 + 5 == 9)
    print("测试完成")
