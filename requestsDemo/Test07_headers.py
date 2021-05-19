import requests

url = "http://ihrm-test.itheima.net/api/sys/login"
headers = {
    "Content-Type": "application/json"
}
data = {"mobile": "13800000002", "password": "123456"}
response = requests.post(url=url, json=data, headers=headers)
print(response.json())
