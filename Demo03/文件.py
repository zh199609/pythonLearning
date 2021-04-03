# file = open('file2',encoding="utf-8")#文件句柄
# print(file.read())

# file2 = open('file2','a',encoding="utf-8")
# file2.write("我爱北京天安门\n")
# file2.write("太阳上升")
# file2.close()

# file = open('file',encoding="utf-8")
#
# for lineData in file:
#     print(lineData.strip())
# file.close()
#
# print("分隔符".center(50,"-"))
# file2 = open('file',encoding="utf-8")
# for lineData in file2.readlines():
#     print(lineData.strip())
# file2.close()
# print("分隔符".center(50,"-"))
# file3 = open('file',encoding="utf-8")
# for index,item in enumerate(file3.readlines()):
#     print(index,item.strip())


#正确写法,内存中只保存一行数据
# file = open('file',encoding="utf-8")
# for line in file:
#     print(line.strip())
# file.close()

#文件指针
# file2 = open('file',encoding="utf-8")
# print(file2.tell())
# print(file2.readline())
# print(file2.readline())
# print(file2.readline())
# print(file2.tell())
# #回到某个位置
# file2.seek(0)
# print(file2.readline())
#
# print(file2.encoding)


#r+ 读写
#w+ 写读
#rb wb 二进制文件
# file = open('file','r+',encoding='utf-8')
# print(file.readline())
# print(file.readline())
# file.write("---------------分隔符---------------")

file = open('file','rb')
print(file.readline())


