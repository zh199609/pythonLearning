list_1 = [1, 2, 351, 561, 361, 0, .3, 3, 5, 2, 0, 1]
list_1 = set(list_1)
print(list_1, type(list_1))

list_2 = set([0, 3, 5, 3, 51, 1, 100])
print(list_2)

# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)
# 并集
print(list_1.union(list_2))
print(list_1 | list_2)
# 差集
print(list_1.difference(list_2))
print(list_1 - list_2)
# 子集
list_3 = set([1, 0])
print(list_3.issubset(list_2))
# 对称差集
print(list_1 ^ list_2)
print("------------------------------------------")
list_3.add(999)
list_3.update([0,1,999,99999])
print(list_3)
list_3.remove(99999)
print(list_3)
print(1 in list_3)
print(1 not in list_3)

