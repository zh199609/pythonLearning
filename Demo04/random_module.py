import random

print(random.random())
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
