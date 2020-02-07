import time

user, pwd = 'zl', '1120'


def auth(type):
    print("auth type:", type)
    def outer_wrapper(func):
        def wrapper(*args, **kwargs):
            username = input("Username:").strip()
            password = input("Password:").strip()
            if user == username and pwd == password:
                print("user and pwd has passed authentication")
                result = func(*args, **kwargs)
            else:
                exit("Invalid user and pwd")
            return result

        return wrapper

    return outer_wrapper


def index():
    print("welcome to index page")


@auth(type="local")
def home():
    print("welcome to home page")


@auth(type="server")
def bbs():
    print("welcome to bbs page")
    return "欢迎来到bbs"


index()
home()
print(bbs())
