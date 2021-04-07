import copy
names =['user01','user02','user03','user04','user05','user06']
print(names[1:])#切片
print(names[-2:])
print(names[-2])
names.append('user07')
names.insert(1,'user08')
print(names)
names[0]='user01_update'
print(names)
#删除
names.remove('user08')
names.pop()
del names[0]

names2 =[1,2,3,4,5,6]
names.extend(names2)
print(names)
del names2
# print(names2)
names[0] = ['a','b']
names3 = names.copy() #只拷贝一级
names[0][0]='A'
print(names3)
print(names)

#深拷贝
names4 = copy.deepcopy(names)

