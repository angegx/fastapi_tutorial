# _*_ coding: UTF-8 _*_
"""
@Project ：fastapi_tutorial
@Time    : 2025-04-19 下午2:33
@Author  : Ange
@Site    : ange.cool
@File    : config.py
@Version : v1.0
@Software: PyCharm
@Email   : angegx.com@gmail.com 
@description : 项目配置文件
"""

import os
from pydantic_settings import BaseSettings
from typing import List


class Config(BaseSettings):
    # 调试模式
    APP_DEBUG: bool = True
    # 项目信息
    VERSION: str = "0.0.1"
    # 项目名称
    PROJECT_NAME: str = "fastapi_tutorial"
    # 项目描述
    DESCRIPTION: str = '<a href="/redoc" target="_blank">redoc</a>'
    # 静态资源目录
    STATIC_DIR: str = os.path.join(os.getcwd(), "static")
    # 静态文件目录
    TEMPLATE_DIR: str = os.path.join(STATIC_DIR, "templates")
    # 跨域请求
    CORS_ORIGINS: List = ["*"]
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List = ["*"]
    CORS_ALLOW_HEADERS: List = ["*"]

    # Session
    SECRET_KEY = "session"
    SESSION_COOKIE = "session_id"
    SESSION_MAX_AGE = 14 * 24 * 60 * 60

    # Jwt
    JWT_SECRET_KEY = "f255eb1987ab4aa092ad2f3ac5cd591226709733ecdf9cadfbe94b22fa3f808e"
    JWT_ALGORITHM = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES = 24 * 60

    SWAGGER_UI_OAUTH2_REDIRECT_URL = "/api/v1/test/oath2"

    # 二维码过期时间
    QRCODE_EXPIRE = 60 * 1


settings = Config()
