import requests

# 创建session
session = requests.Session()
# 获取验证码
response = session.get("http://localhost/index.php?m=Home&c=User&a=verify")

# 登录
login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "15824349156",
    "password": "123456",
    "verify_code": "8888"
}
login_response = session.post(url=login_url, data=login_data)
print(login_response.json())


#获取我的订单
order_response = session.get("http://localhost/Home/Order/order_list.html")
print(order_response.text)
