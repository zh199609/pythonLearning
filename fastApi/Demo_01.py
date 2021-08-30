# -*- coding: utf-8 -*-
# @Project: pythonLearning
# @File    : Demo_01.py
# @Author  : Administrator
# @Time    : 2021-08-30 16:54:42
# @Desc    :
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


# @app.post("/login")
def login(user_name: str):
    user_name.lower()
    print()
