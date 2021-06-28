import random

from bs4 import BeautifulSoup

print(random.random())

r = random.sample('asdgasdgkuhuoweoirjho', 4)
print(r)
rand = ''.join(r)
print(rand)

html = """
<html>
<head><title>黑马程序员</title></head>
<body>
<p id="test01">软件测试<span>我是span</span></p>
<p id="test02">2020年</p>
<a href="/api.html">接口测试</a>
<a href="/web.html">Web自动化测试</a>
<a href="/app.html">APP自动化测试</a>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
print("获取title对象：", soup.title)
print("获取title的标签名：", soup.title.name)
print("获取title的值：", soup.title.string)

print('获取p标签对象', soup.p)
print('获取所有p标签对象', soup.find_all('p'))
print('获取a标签对象', soup.a)

print('获取p标签的id:', soup.p['id'])
print('获取p标签的值:', soup.p.contents)


