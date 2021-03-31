import json

info = {
    'name': "张磊",
    "age": 25
}
f = open("test.txt", "w", encoding="utf-8")
print(str(info))
# f.write(str(info))
# 序列化
json.dump(info, f, ensure_ascii=False)
f.close()

# 恢复
f = open("test.txt", "r", encoding="utf-8")
# data = f.read()
# print(data)
# print(eval(data)["name"])
# 反序列化
# print(json.loads(data)["name"])
data = json.load(f)
print(data['name'])
print("-----------------------------")


def say(name):
    print("hello:", name)
