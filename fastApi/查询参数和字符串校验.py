# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 查询参数和字符串校验.py
# @Author  : Administrator
# @Time    : 2021-08-31 12:41:51
# @Desc    :
from typing import Optional, List

from fastapi import FastAPI, Query

app = FastAPI()


@app.post("/items")
def read_items(q: Optional[str] = Query(None, max_length=50,alias='qq')):
    """
    Query 显式地将其声明为查询参数。
    由于我们必须用 Query(None) 替换默认值 None，Query 的第一个参数同样也是用于定义默认值。 q: str = Query(None) =q: str = None

    当你在使用 Query 且需要声明一个值是必需的时，可以将 ... 用作第一个参数值
    alias给参数取别名 ，在请求时参入的参数就是alias
    """
    result = {"items": [{'item_id': 100}, {"item_id": 200}]}
    if q:
        result.update({"q": q})
    return result


@app.post('/items2')
def read_items2(q: Optional[List[str]] = Query(None)):
    """
    要声明类型为 list 的查询参数，如上例所示，你需要显式地使用 Query，否则该参数将被解释为请求体。
    """
    return q
