import requests

login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_data = {"mobile": "13800000002", "password": "123456"}
response = requests.post(url=login_url, json=login_data)
print(response.json())
