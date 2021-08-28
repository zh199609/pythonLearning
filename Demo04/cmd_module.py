# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : cmd_module.py
# @Author  : Administrator
# @Time    : 2021-08-27 10:49:24
# @Desc    : 执行cmd命令

#方法一：os.system

#方法二：os.popen(执行的命令)，popen可以获取输出的信息内容，它是一个对象，可以通过 .read() 去读取
import os

print(os.popen("pip show selenium").read())
