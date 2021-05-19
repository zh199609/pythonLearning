import requests

if __name__ == '__main__':
    response = requests.get("http://www.baidu.com")
    # 查看响应数据编码格式
    print("返回编码：", response.encoding)
    print(response.text)
    response.encoding = "utf-8"
    print(response.text)
