# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 请求体-嵌套模型.py
# @Author  : Administrator
# @Time    : 2021-08-31 15:41:30
# @Desc    :
from typing import Optional, List, Set

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    tags: List[str] = []
    sets: Set[int] = set()
    image: Optional[Image] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results
