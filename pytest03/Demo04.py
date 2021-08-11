import pytest

"""
在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
可以叠加多个 @pytest.mark.usefixtures() ，先执行的放底层，后执行的放上层
可以传多个fixture参数，先执行的放前面，后执行的放后面
如果fixture有返回值，用 @pytest.mark.usefixtures() 是无法获取到返回值的，必须用传参的方式（方式一）
"""

# 调用方式一
# 将fixture名称作为测试用例函数的输入参数
@pytest.fixture
def login():
    print("login--输入账号，密码先登录")


def test_s1(login):
    print("test_s1：登录之后其他动作…………")


def test_s2():
    print("test_s2：登录之后其他动作…………")


@pytest.fixture
def login2():
    print("login2--please输入账号，密码先登录")

#调用方式二
@pytest.mark.usefixtures("login2", "login")
def test_s3():
    print("test_s3：登录之后其他动作…………")

#  调用方式三
@pytest.fixture(autouse=True)
def login3():
    print("login3--自动登录")


# 不是test开头，加了装饰器也不会执行fixture
@pytest.mark.usefixtures("login2")
def loginss():
    print(123)


if __name__ == '__main__':
    pytest.main(["-q", "-s", "-ra"])
