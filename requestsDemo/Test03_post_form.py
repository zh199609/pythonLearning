import requests

login_url = "http://localhost/index.php?m=Home&c=User&a=do_login"
login_data = {
    "username": "15824349156",
    "password": "123456",
    "verify_code": "88888"
}
response = requests.post(url=login_url, data=login_data)
print(response.json())
