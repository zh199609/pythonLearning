
print(all([11, 0]))
print(any([11, 0, "fadf4"]))
print(bool("sfd"))

b = bytearray("abcd", encoding="utf-8")
print(b[0])
b[0] = 65
print(b)

print(divmod(10, 2))



calc = lambda n: print(n)
calc(2)

print("--------------")
# 过滤
res = filter(lambda n: n > 5, range(10))
for item in res:
    print(item)
print("------------------")
map = map(lambda n: n * 2, range(10))
for item in map:
    print(item)

a = {
    6: 2,
    8: 0,
    1: 4,
    3: 6,
    -6: 45,
    99: 11,
    25: 28
}
print(a)
# 模式按key排序
print(sorted(a.items()))
# 按bal排序
print(sorted(a.items(), key=lambda x: x[1]))