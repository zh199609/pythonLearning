# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 查询参数.py
# @Author  : Administrator
# @Time    : 2021-08-30 18:29:01
# @Desc    : 查询参数
from typing import Optional

from fastapi import FastAPI

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
app = FastAPI()


@app.get("/items/")
def read_item(skip: int = 0, limit: int = 0):
    print(skip, type(skip))
    print(limit, type(limit))
    return fake_items_db[skip: skip + limit]


# 可选参数q
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
