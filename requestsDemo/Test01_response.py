import requests

if __name__ == '__main__':
    response = requests.get("http://www.baidu.com")
    # 查看响应数据编码格式
    print("返回编码：", response.encoding)
    print(response.text)
    response.encoding = "utf-8"
    print(response.text)
    print("响应头：", response.headers)
    print("获取指定cookie：", response.cookies.get("BDORZ"))
    print("获取字节形式的响应内容：",response.content)
