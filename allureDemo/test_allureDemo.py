import allure
import pytest


@allure.title("前置操作：登录")
@pytest.fixture
def test_loginss(request):
    param = request.param
    name = param.get('name')
    pwd = param.get('pwd')
    allure.attach(f"这是测试用例传的参数{param}")
    print(name, pwd, param)
    yield name, pwd


@pytest.mark.parametrize('test_loginss', [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"}], indirect=True)
def test_success_login(test_loginss):
    name, pwd = test_loginss
    allure.attach(f'账号{name},密码{pwd}')
