_username = 'zh'
_password = '123'
user = input('请输入用户名：')
pwd = input('请输入密码：')
if user == _username and pwd == _password:
    print("登录成功用户%s", user)
else:
    print("错误了")

print(user, pwd)
