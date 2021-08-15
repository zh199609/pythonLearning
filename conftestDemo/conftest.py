"""
最顶层的conftest，一般写全局的fixture，在Web UI自动化中，可能会初始化driver
"""
import pytest


@pytest.fixture(scope='session')
def login():
    print("===登录功能，返回账号，token===")
    name = 'testyy'
    token = 'npoi12afag'
    yield name, token
    print('===退出登录===')


@pytest.fixture(autouse=True)
def get_info(login):
    name, token = login
    print(f'==每个测试用例都调用外层fixture,打印用户token:{token}==')


@pytest.fixture(autouse=True)
def logger(login):
    name, token = login
    print(f'logger记录token:{token}==')
