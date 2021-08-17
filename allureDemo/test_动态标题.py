import os

import allure
import pytest


@pytest.fixture
def login(request):
    """
    登录
    :param request:
    :return:
    """
    param = request.param
    print(f"账号是:{param['username']},密码是:{param['pwd']}")
    return {'code': 0, 'msg': "success"}


datas = [
    {"username": "name1", "pwd": "pwd1"},
    {"username": "name2", "pwd": "pwd2"},
    {"username": "name3", "pwd": "pwd3"}
]

ids = [
    "username is name1,pwd is pwd1",
    "username is name2,pwd is pwd2",
    "username is name3,pwd is pwd3"
]


@allure.story('登录功能')
@allure.title(f'登录测试用例-{login}')
@pytest.mark.parametrize('login', datas, ids=ids, indirect=True)
def test_login(login):
    """
     登录测试用例1
    """
    assert login['code'] == 0


if __name__ == '__main__':
    pytest.main(['-sq', 'test_动态标题.py', '--alluredir', './allure', '--clean-alluredir'])
    os.system('allure serve allure')
