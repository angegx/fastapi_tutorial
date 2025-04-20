# _*_ coding: UTF-8 _*_
"""
@Project ：fastapi_tutorial
@Time    : 2025-04-19 下午2:16
@Author  : Ange
@Site    : ange.cool
@File    : app.py
@Version : v1.0
@Software: PyCharm
@Email   : angegx.com@gmail.com 
@description :
    app运行时文件
    FastAPI应用程序的入口文件
    主要用于创建FastAPI实例和配置路由
    使用uvicorn作为ASGI服务器运行FastAPI应用程序
"""

from fastapi import FastAPI
from config import settings

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}
