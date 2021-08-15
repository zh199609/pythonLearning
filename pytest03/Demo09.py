"""
pytest.skip(msg="",allow_module_level=False)
当 allow_module_level=True 时，可以设置在模块级别跳过整个模块
"""
import sys

import pytest

if sys.platform.startswith('win'):
    pytest.skip('skipping windows-only tests', allow_module_level=True)


@pytest.fixture
def login():
    print('登录')


@pytest.mark.usefixtures('login')
def test_case1():
    print("我是测试用例11111")
