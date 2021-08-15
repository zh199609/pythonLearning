import pytest
from lockfile import FileLock

"""
分布式执行测试
pytest -s -n auto

可以指定需要多少个CPU来跑用例
pytest -s -n 2


pytest-xdist是可以和pytest-html很好的相结合
pytest -s -n auto --html=report.html --self-contained-html
"""


# @pytest.fixture(scope='session')
# def login():
#     print("==登录功能，返回账号，token==")
#     name = 'testyy'
#     token = 'npoi112236'
#     yield name, token
#     print("==退出登录！==")


@pytest.fixture(scope="session")
def login():
    print("====登录功能，返回账号，token===")
    with FileLock("session.lock", encoding='utf-8'):
        name = "testyy"
        token = "npoi213bn4"
        # web ui自动化
        # 声明一个driver，再返回

        # 接口自动化
        # 发起一个登录请求，将token返回都可以这样写

    yield name, token
    print("====退出登录！！！====")
