# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : list用作数据结构.py
# @Author  : Administrator
# @Time    : 2021-08-29 14:17:20
# @Desc    :
# 模拟栈   先进后出，后进先出
from collections import deque

stack = [1, 2, 3, 4, 5]

stack.append(6)
stack.append(7)

print(stack)
stack.pop()
print(stack)

# 模拟队列，先进先出，后进后出 使用 collections.deque ，它被设计成可以快速从两端添加或弹出元素
queue = deque(stack)

queue.append('7')
queue.append('8')
print(queue)

# 移除队列
queue.popleft()
print(queue)

