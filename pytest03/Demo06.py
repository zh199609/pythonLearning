"""
fixture之yield实现teardown
用fixture实现teardown并不是一个独立的函数，而是用 yield 关键字来开启teardown操作
"""
import pytest


@pytest.fixture(scope="session")
def open():
    print("===打开浏览器===")
    test = "测试变量是否返回"
    yield test
    print("===关闭浏览器===")


@pytest.fixture
def login(open):
    print(f"输入账号，密码先登录{open}")
    name = '我是账号'
    pwd = '我是密码'
    age = '我是年龄'
    yield name, pwd, age
    print("登录成功")


def test_s1(login):
    print("===用例1===")
    # 返回的是一个元组
    print(login)
    # 分别赋值给不同变量
    name, pwd, age = login
    print("返回值：", name, pwd, age)
    assert name == '我是账号'


def test_s2(login):
    print("===用例2===")
    print(login)
