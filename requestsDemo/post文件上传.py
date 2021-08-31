# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : post文件上传.py
# @Author  : Administrator
# @Time    : 2021-08-30 20:51:34
# @Desc    :
import requests

url = 'http://httpbin.org/post'  # 上传文件接口
files = {
    'file': ('test.png',  # 文件名称
             open('E:/内部项目部署.docx', 'rb'),  # 文件路径
             'image/png',  # 文件类型
             {'Expires': '0'}  # 其他参数,非必传
             )
}  # => 打开上传文件并且加入文件相关参数

data = {
    "name": "test"
}

# data传入请求参数dict,files传入待上传文件参数dict
r = requests.post(url, data=data, files=files)
print(r.json())
