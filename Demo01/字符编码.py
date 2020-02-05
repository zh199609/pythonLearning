import sys

print(sys.getdefaultencoding())

name = "你好"
s= name.encode('gbk')
print(s)
print(name.encode('utf-8'))
# s_gbk = s.encode("gbk")
# print(s_gbk)
