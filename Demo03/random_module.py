import random

print(random.random())

print(random.randint(1, 3))

# 没有3
print(random.randrange(1, 3))

print(random.choice('hello'))
print(random.choice([1, 3, 35, 5, 6, 84, 6984, 1]))

# 序列中随机取两个
print(random.sample('hello', 2))

# 指定区间 浮点数
print(random.uniform(1, 10))

l = [i for i in range(1, 10)]
random.shuffle(l)
print(l)

check_code = ''
for i in range(4):
    current = random.randrange(0, 4)
    if current == i:
        check_code += chr(random.randint(65, 90))
    else:
        check_code += str(random.randint(0, 9))
print(check_code)
