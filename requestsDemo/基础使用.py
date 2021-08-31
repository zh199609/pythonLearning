# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 基础使用.py
# @Author  : Administrator
# @Time    : 2021-08-30 20:38:04
# @Desc    :
import json

import requests

url = 'http://172.16.208.78:20017/CCEggshell/businessLabel/businessLabelList'
cookies = {
    "JSESSIONID": "D32C821BB93A53D3A8DDD5434567717B",
    "IAMAppsession_E35A3069A526435395B0ECAC6B035B88": "95b574f5af46416583532b62650506ec"
}
headers = {
    "Content-Type": "application/json"
}
data = {

}
res = requests.get(url, headers=headers, cookies=cookies)
print('请求url:', res.url)
print('响应内容json格式：', json.dumps(res.json()))
print('响应内容字符串格式：', res.text)
print('响应内容二进制格式:', str(res.content))
print('响应码：', str(res.status_code))
