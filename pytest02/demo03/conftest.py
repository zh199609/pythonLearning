import pytest


@pytest.fixture(scope="function", autouse=True, params=['成龙', '甄子丹'])
def my_fixture(request):
    """
    scope:被@pytest.fixture标记的方法的作用域，function（默认）、class、module、package/session
    params:参数化,支持list tuple,字典列表，字典元祖
    autouse:自动执行，默认False
    ids:当使用params参数化是，给每一个值设置一个变量名
    name：表示被@pytest.fixture标记的方法取一个别名
    """
    print("这是前置的方法，可以实现部分及全部用例的前置")
    yield request.param
    print("这是后置的方法，可以实现部分及全部用例的后置")
    # return request.param


@pytest.fixture(scope="function", autouse=False)
def user_fixture(request):
    print("用户管理前置")
    yield
    print("用户管理后置")
