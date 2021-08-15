"""
pytest.fixture() 允许fixture有参数化功能（后面讲解）
 @pytest.mark.parametrize 允许在测试函数或类中定义多组参数和fixtures
 pytest_generate_tests 允许定义自定义参数化方案或扩展（拓展）
"""
import pytest


@pytest.mark.parametrize(['test_input', 'expected'], [('6+6', 12), ('8+8', 16), ('10+10', 20)])
def test_eval(test_input, expected):
    print(f"f测试数据{test_input},期望结果{expected}")
    assert eval(test_input) == expected


"""
当装饰器 @pytest.mark.parametrize 装饰测试类时，会将数据集合传递给类的所有测试用例方法
"""

"""
笛卡尔积”，多个参数化装饰器
"""
data_1 = [1, 2, 3]
data_2 = ['a', 'b', 'c']


@pytest.mark.parametrize('a', data_1)
@pytest.mark.parametrize('b', data_2)
def test_parametrize(a, b):
    print(f"笛卡尔积，测试数据{a}:{b}")


# 参数化，传入字典
data_dic = (
    {
        "user": 1,
        "pwd": 2
    },
    {
        "user": 3,
        "pwd": 4
    }
)


@pytest.mark.parametrize('dic', data_dic)
def test_parametrize_dict(dic):
    print(f"测试数据为\n{dic}")
    print(f"user:{dic.get('user')}")


# 参数化标记

@pytest.mark.parametrize(['input', 'expected'], [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6*9", 54, marks=pytest.mark.xfail),
    pytest.param("6*9", 42, marks=pytest.mark.skip),
])
def test_mark(input, expected):
    assert eval(input) == expected


# 参数化，增加可读性
data_3 = [
    (1, 2, 3),
    (4, 5, 9)
]

ids = ["a:{}+b:{} = expect:{}".format(a, b, expect) for a, b, expect in data_3]


@pytest.mark.parametrize(['a', 'b', 'expect'], data_3,ids=ids)
class TestParametrize(object):
    def test_parametrize_1(self, a, b, expect):
        print('测试函数1测试数据为{}-{}'.format(a, b))
        assert a + b == expect

    def test_parametrize_2(self, a, b, expect):
        print('测试函数2测试数据为{}-{}'.format(a, b))
        assert a + b == expect
