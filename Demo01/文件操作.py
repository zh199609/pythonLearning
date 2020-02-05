# data = open("file",encoding="utf-8").read()
f = open("file2", mode="a", encoding="utf-8")  # 文件句柄
# model = 'a'  append 追加
f.write("追加内容\n")
f.write("aaaaaaaaaaa")
f.write("bbbbbbbbbbbbbbbbbbbbb")
# f.write("我爱ui")
# data2 = f.read()
# print(data2)

print("------------")
f.close()

ff = open('file', 'r', encoding="utf-8")
for line in ff.readlines():
    print(line.strip())
ff.close()

for index, item in enumerate(range(10, 20)):
    print("index:%s,item:%s" % (index, item))

print("=--------------")

# 效率最高  内存中保存一行
fff = open('file', 'r', encoding="utf-8")
for line in fff:
    print(line)
fff.close()
print("--------------")
fff = open('file', 'r', encoding="utf-8")
print(fff.encoding)
# 读取文件指针位置
print(fff.tell())
# fff.seek(3)
print(fff.read(10))
print(fff.tell())
# 指针回到指定位置
fff.seek(0)
print(fff.tell())
fff.close()
