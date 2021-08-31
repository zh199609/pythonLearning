# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 请求体-多个参数.py
# @Author  : Administrator
# @Time    : 2021-08-31 13:51:46
# @Desc    : 请求体-多个参数
from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None

#请求体-多个参数
@app.post('/items/{item_id}')
def update_item(item_id: int, item: Item, user: User, importance: int = Body(...)):
    """
        使用 Body 指示 FastAPI 将其作为请求体的另一个键进行处理。
        ...代表必填参数
    """
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results
