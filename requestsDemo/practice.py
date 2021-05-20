import requests

base_url = "http://ihrm-test.itheima.net"
login_url = base_url + "/api/sys/login"
login_data = {
    "mobile": "13800000002", "password": "123456"
}
login_resp = requests.post(url=login_url, json=login_data)
print(login_resp.json())

auth_token = "Bearer " + login_resp.json().get("data")
user_url = base_url + "/api/sys/user/" + "1395279022610571264"
headers = {
    "Authorization": auth_token
}
user_resp = requests.get(url=user_url, headers=headers)
print(user_resp.text)
