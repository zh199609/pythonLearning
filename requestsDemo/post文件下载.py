# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : post文件下载.py
# @Author  : Administrator
# @Time    : 2021-08-30 21:00:12
# @Desc    :
import requests

down_url = 'https://www.imooc.com/mobile/appdown'
res = requests.post(down_url)
# print(res.content)
with open('./imooc.apk','wb') as f:
    f.write(res.content)