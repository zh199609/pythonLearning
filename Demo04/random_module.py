import random
import string

print(random.random())  # 返回浮点数[0.0,1.0)
print(random.randint(1, 3))  # [1,3]
print(random.randrange(1, 3))  # [1,3)

check_code = ''
for i in range(4):
    current = random.randrange(0, 4)  # 0,1,2,3
    if current != i:
        temp = chr(random.randint(65, 90))
    else:
        temp = random.randint(0, 9)
    check_code += str(temp)
print(check_code)

# random.uniform(a, b)   返回一个随机浮点数 N
print(random.uniform(10, 20))

# random.choice 从非空序列 seq 返回一个随机元素
li = [random.randint(0, 100) for i in range(20)]
li2 = (random.randint(0, 100) for i in range(20))

print("从非空序列中返回一个随机元素：", random.choice(li))
print("从非空序列中返回一个随机元素：", random.choice('abcdefg'))
print(" string 模块返回的大小写字母字符串", string.ascii_letters)
print(" string 模块返回的数字字符串", string.digits)
print(" string 模块返回的大写字母字符串", string.ascii_uppercase)

# random.shuffle
li3 = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(li3)
print("将序列 x 随机打乱位置:", li3)

# random.sample
# 从 population 中取 k 个元素，组成新的列表并返回,每次取元素都是不重复的
print(random.sample(li3, 3))
print(random.sample(string.ascii_letters, 3))
