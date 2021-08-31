# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 请求体-字段.py
# @Author  : Administrator
# @Time    : 2021-08-31 15:35:16
# @Desc    : 请求体-字段
from typing import Optional

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    desc: Optional[str] = Field(
        None, title='The desc of the item', max_length=100
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(..., embed=True)):
    results = {"item_id": item_id, "item": item}
    return results
