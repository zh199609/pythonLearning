import urllib.parse

import requests

# 通过url传递参数
response = requests.get("http://localhost/Home/Goods/search.html?q=手机")

# 通过params传递参数
response2 = requests.get("http://localhost/Home/Goods/search.html", params="q=手机")

# 字典
params3 = {
    "q": "手机"
}
response3 = requests.get("http://localhost/Home/Goods/search.html", params=params3)

# print("响应：", response.text)
# print("响应：", response2.text)
print("响应：", response3.text)

if __name__ == '__main__':
    url = "http://localhost/Home/Goods/search.html?q=手机"
    print(urllib.parse.quote(url))
    encodingUrl = "http%3A//localhost/Home/Goods/search.html%3Fq%3D%E6%89%8B%E6%9C%BA"
    print(urllib.parse.unquote(encodingUrl))
