# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : 路径参数.py
# @Author  : Administrator
# @Time    : 2021-08-30 17:51:47
# @Desc    :
from enum import Enum

from fastapi import FastAPI

app = FastAPI()


# http://127.0.0.1:8000/items/foo
@app.get("/items/{item_id}")
def read_item(item_id: str):
    return {"item_id": item_id}


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    return model_name
