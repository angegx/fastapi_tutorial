# _*_ coding: UTF-8 _*_
"""
@Project ：fastapi_tutorial
@Time    : 2025-04-19 下午4:08
@Author  : Ange
@Site    : ange.cool
@File    : Events.py
@Version : v1.0
@Software: PyCharm
@Email   : angegx.com@gmail.com 
@description : 项目事件处理
"""

from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql
from database.redis import sys_cache, code_cache
from aioredis import Redis


def startup(app: FastAPI) -> Callable:
    """
    FastApi 启动完成事件
    :param app: FastAPI
    :return: start_app
    """

    async def app_start() -> None:
        # APP启动完成后触发
        print("fastapi已启动")
        # 注册数据库
        await register_mysql(app)
        # 注入缓存到app state下·
        app.state.cache = await sys_cache()
        app.state.code_cache = await code_cache()

        pass

    return app_start


def stopping(app: FastAPI) -> Callable:
    """
    FastApi 停止事件
    :param app: FastAPI
    :return: stop_app
    """

    async def stop_app() -> None:
        # APP停止时触发
        print("fastapi已停止")
        cache: Redis = await app.state.cache
        code: Redis = await app.state.code_cache
        await cache.close()
        await code.close()

    return stop_app
