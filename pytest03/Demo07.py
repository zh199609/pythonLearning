"""
用例执行完成后，每条用例都有自己的状态，常见的状态有

passed：测试通过
failed：断言失败
error：用例本身写的质量不行，本身代码报错（譬如：fixture不存在，fixture里面有报错）
xfail：预期失败，加了 @pytest.mark.xfail()

"""

# error的例子
import pytest


def pwd():
    print('获取用户名')
    a = "yygirl"
    assert a == 'zlboy'


def test_1(pwd):
    assert user == 'yygirl'


# error的例子二 fixture里面断言失败，所以fixture会报错；
@pytest.fixture
def user():
    print("获取用户名")
    a = 'yygirl'
    assert a == 'yygirl123'
    return a


def test_2(user):
    assert user == 'yygirl'


# failed例子
@pytest.fixture()
def pwd2():
    print("获取密码")
    a = 'yygirl'
    return a


def test_3(pwd2):
    assert pwd2 == 'zlboy'


# failed例子二
def test_4(pwd2):
    raise NameError
    assert pwd2 == 'yygirl'


# xfail列子
# 断言装饰器
@pytest.mark.xfail(raises=ZeroDivisionError)
def test_f():
    1 / 0
