"""
fixture 传参数 request的详细使用

假设不同的用例想登录不同的测试账号，那么登录fixture就不能把账号写死，需要通过传参的方式来完成登录操作
"""
import pytest


@pytest.fixture
def login(request):
    name = request.param
    print(f"==账号是：{name}==")
    return name


def getData_1():
    data_1 = ['pyy1', 'zl2']
    return data_1


ids = [f'login_test_name is:{name}' for name in getData_1()]


# 添加  indirect=True  参数是为了把 login 当成一个函数去执行，而不是一个参数，并且将data当做参数传入函数
# def test_name(login) ，这里的login是获取fixture返回的值
#
@pytest.mark.parametrize('login', getData_1(), ids=ids, indirect=True)
def test_name(login):
    print(f"测试用例的登录账号是：{login}")


# 多个参数
@pytest.fixture
def logins(request):
    param = request.param
    print(f"账号是：{param['username']},密码是：{param['pwd']}")
    return param


def getData_2() -> list:
    data = [
        {"username": "name1", "pwd": "pwd1"},
        {"username": "name2", "pwd": "pwd2"},
    ]
    return data


@pytest.mark.parametrize('logins', getData_2(), indirect=True)
def test_name_pwd(logins):
    print(f"测试用例登录的账号是：{logins['username']},密码是：{logins['pwd']}")


# 多个fixture（只加一个装饰器）
@pytest.fixture()
def input_user(request):
    username = request.param
    print("登录的账户是：%s" % username)
    return username


@pytest.fixture
def input_pwd(request):
    pwd = request.param
    print("登录的密码是：%s" % pwd)
    return pwd


data_3 = [
    ("name1", "pwd1"),
    ("name2", "pwd2")
]


@pytest.mark.parametrize(['input_user', 'input_pwd'], data_3, indirect=True)
def test_more_fixture(input_user, input_pwd):
    print("fixture返回的内容是：", input_user, input_pwd)


data_user = ['name1', 'name2']
data_pwd = ['pwd1', 'pwd2']


# 多个fixture（叠加装饰器）
@pytest.mark.parametrize('input_user', data_user, indirect=True)
@pytest.mark.parametrize('input_pwd', data_pwd, indirect=True)
def test_more_fixtures(input_user, input_pwd):
    print("fixture返回的内容是：", input_user, input_pwd)
