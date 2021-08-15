"""
pytest 可以支持自定义标记，自定义标记可以把一个 web 项目划分多个模块，然后指定模块名称执行
譬如我可以标明哪些用例是window下执行的，哪些用例是mac下执行的，在运行代码时候指定mark即可
"""
import pytest


@pytest.mark.weibo
def test_weibo():
    print("测试微博")


@pytest.mark.toutiao
def test_toutiao():
    print("测试头条")


@pytest.mark.toutiao
def test_toutiao2():
    print("再次测试头条")


def testnoMark():
    print("没有标记测试")


#>pytest -s -m weibo Demo10.py

