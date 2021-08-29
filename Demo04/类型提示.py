# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 类型提示.py
# @Author  : Administrator
# @Time    : 2021-08-29 15:51:00
# @Desc    :
from typing import List, Dict, Tuple

num: int = 1

bool_var: bool = True

primes: List[int] = [1]


def greeting(name: str) -> str:
    return name


# 取别名
ConnectionOptions = Dict[str, str]
Address = Tuple[str, int]
Server = Tuple[Address, ConnectionOptions]


def broadcast_message(message: str, servers: Server) -> None:
    print(message, servers)
