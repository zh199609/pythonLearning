# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : Demo_基础.py
# @Author  : Administrator
# @Time    : 2021-08-30 16:42:36
# @Desc    :
import requests

url = 'http://172.16.208.248:9066/iamApi/doLogin'
param = {
    "security_username": "1",
    "security_password": "1",
    "app_id": "B92F970DE1064B97BE1876A8B05BED11",
    "queryParam": "ECC368A25826F08C76A7DB14C9AC5D55B8A42CCB644D314C341B87D85907B30870AEE965720CAC46ADDB8266FFF4ABAE",
    "Submit": "Login"
}
res = requests.get(url)
print(res.text)
