from time import sleep

import pytest


@pytest.mark.parametrize('n', list(range(5)))
def test_get_info(login, n):
    """
    当然，在方法声明的下一行这样子写，也算一种添加description的方式哦
    """
    sleep(1)
    name, token = login
    print("***基础用例，获取用户个人信息***", n)
    print(f'用户名：{name},token:{token}')
