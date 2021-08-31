# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 请求体.py
# @Author  : Administrator
# @Time    : 2021-08-31 12:30:06
# @Desc    : 请求体参数
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    desc: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items")
def create_item(item: Item):
    print(item)
    return item

#请求体+路径参数
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}

#请求体 + 路径参数 + 查询参数
@app.put("/items2/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result

