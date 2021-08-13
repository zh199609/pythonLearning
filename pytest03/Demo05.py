"""
fixture的实例化顺序
较高 scope 范围的fixture（session）在较低 scope 范围的fixture（ function 、 class ）之前实例化【session > package > module > class > function】
具有相同作用域的fixture遵循测试函数中声明的顺序，并遵循fixture之间的依赖关系【在fixture_A里面依赖的fixture_B优先实例化，然后到fixture_A实例化】
自动使用（autouse=True）的fixture将在显式使用（传参或装饰器）的fixture之前实例化

"""
import pytest

order = []


@pytest.fixture(scope="session")
def s1():
    order.append("s1")


@pytest.fixture(scope="module")
def m1():
    order.append("m1")


@pytest.fixture
def f1(f3, a1):
    # 先实例化f3,在实例化a1,最后实例化f1
    order.append("f1")
    assert f3 == 123


@pytest.fixture
def f3():
    order.append("f3")
    a = 123
    yield a
    print("f3 end f3 end f3 end f3 end")


@pytest.fixture
def a1():
    print("a1a1a1a1a1a1a1")
    order.append("a1")


@pytest.fixture
def f2():
    print("f2f2f2f2f2f2")
    order.append("f2")


def test_order(f1, m1, f2, s1):
    print(order)
    assert order == ['s1', 'm1', 'f3', 'a1', 'f1', 'f2']

