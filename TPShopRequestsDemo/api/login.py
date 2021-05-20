class LoginAPI:
    # 初始化
    def __init__(self):
        self.verify_url = "http://localhost/index.php?m=Home&c=User&a=verify"
        self.login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"

    # 获取验证码接口
    def get_verify_code(self, session):
        return session.get(self.verify_url)

    # 登录接口
    def login(self, session, username, password, verify_code):
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        return session.post(url=self.login_url, data=login_data)
