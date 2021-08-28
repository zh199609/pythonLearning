import os
path = os.getcwd()
print(os.getcwd())#获取当前工作目录，即当前python脚本工作的目录路径
print("获取当前绝对路径：",os.path.abspath(os.getcwd()))
print(os.pardir)#获取当前目录的父目录字符串名：('..')
print(os.environ)
print(os.path.abspath(".")) #返回path规范化的绝对路径

print(os.path.split('os_module.py'))#将path分割成目录和文件名二元组返回
print(os.path.dirname('os_module.py'))#返回path的目录。其实就是os.path.split(path)的第一个元素
#os.path.basename(path)  返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
print(os.path.exists('os_module.py'))#如果path存在，返回True；如果path不存在，返回False


print("获取当前路径下所有文件、文件夹：",os.listdir(os.getcwd()))

# 创建文件方式一
f = os.open(path + "/test.txt", flags=os.O_CREAT | os.O_RDWR )


