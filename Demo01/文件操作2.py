import time, sys

# for i in range(20):
#     sys.stdout.write("#")
#     sys.stdout.flush()
#     time.sleep(0.1)


f = open('file2', mode='w', encoding='utf-8', buffering=4096)
f.write("1111111111\n")
f.write("2222222222\n")
f.write("3333333333\n")
f.write("4444444444\n")
f.flush()
f.close()
print(f.closed)

# 读写
f = open('file', mode='r+', encoding='utf-8', buffering=4096)
print(f.readline(),f.readline(),f.readline(),f.readline())
f.write("新增内容 woaini")
f.close()

# 写读
f = open('file3', mode='w+', encoding='utf-8', buffering=4096)
f.write("1111111111\n")
f.write("2222222222\n")
print(f.readline())
f.seek(0)   #无法从指定位置写   只能在最后写
f.write("3333333333\n")
print(f.read())
f.close()
print("-----------------")
# 二进制读取文件
f = open('file','rb')
print(f.readline())