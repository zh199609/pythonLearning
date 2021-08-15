"""
@pytest.mark.skip
"""
import sys

import pytest


@pytest.fixture(autouse=True)
def login():
    print("===登录===")


def tet_case01():
    print('tet_case01')


@pytest.mark.skip(reason='不执行改用里，因为没有写好')
def test_case02():
    print('test_case02')


"""
可以将 pytest.mark.skip 和 pytest.mark.skipif 赋值给一个标记变量
在不同模块之间共享这个标记变量
若有多个模块的测试用例需要用到相同的 skip 或 skipif ，可以用一个单独的文件去管理这些通用标记，然后适用于整个测试用例集
"""
# 标记
skipmark = pytest.mark.skip(reason="不能在window上运行=====")
skipifmark = pytest.mark.skipif(sys.platform == 'win32', reason="不能在window上运行啦啦啦=====")


class Test1:
    def test_1(self):
        print("%% 我是类测试用例1111 %%")

    @pytest.mark.skip(reason="不想执行")
    def test_2(self):
        print("%% 我是类测试用例2222 %%")

    @pytest.mark.skipif(sys.platform == 'win32', reason='does not run on windows')
    def test_3(self):
        print("不能再window上运行")

    @skipmark
    def test_4(self):
        print("标记跳过")
