# 获取验证码
import requests

verifyImage = requests.get("http://localhost/index.php?m=Home&c=User&a=verify")
phpSession = verifyImage.cookies.get("PHPSESSID")
print(phpSession)

login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "15824349156",
    "password": "123456",
    "verify_code": "8888"
}
cookies = {
    "PHPSESSID": phpSession
}
response = requests.post(url=login_url, data=login_data, cookies=cookies)
print(response.json())

# 获取订单
item_url = "http://localhost/Home/Order/order_list.html"
response_item = requests.get(url=item_url, cookies=cookies)
print(response_item.text)
