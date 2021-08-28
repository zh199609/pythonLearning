# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : pathlib_module.py
# @Author  : Administrator
# @Time    : 2021-08-24 17:49:53
# @Desc    : 第三方库pathlib ，替代os
import os

from pathlib import Path

v1 = os.getcwd()
print(v1)

v2 = Path.cwd()
print(v2)
# 获取上层、上上层目录
print(os.path.dirname(os.path.dirname(os.getcwd())))
print(Path.cwd().parent.parent)

# 拼接目录
print(os.path.join(os.path.dirname(os.getcwd()), 'test', 'text.txt'))
print(Path.cwd().parent.joinpath("test", "test.txt"))
