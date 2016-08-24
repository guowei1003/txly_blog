#  coding:utf-8

"""
file: conf.py
author: 曹国伟
content: 此文件为工程配置文件
create date: 2016年8月19日14:09:25
"""
import os
import sys

ROOT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.pardir)
sys.path.append(ROOT_DIR)

#  rides数据库配置
DB = {
    'DB_HOST': "127.0.0.1",
    'DB_NAME': "127.0.0.1",
    'DB_USER': "127.0.0.1",
    'DB_PASSWORD': "127.0.0.1",
}
#  redi缓存配置
config = {
    'CACHE_TYPE': 'redis',
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_REDIS_DB': '',
    'CACHE_REDIS_PASSWORD': ''
}
#  静态文件配置
STATIC_ROOT = os.path.join(ROOT_DIR, "static")
#  模板文件配置
TEMPLATE_ROOT = os.path.join(ROOT_DIR, "templates")
#  存储文件配置
MEDIA_ROOT = os.path.join(ROOT_DIR, "medias")
#  其他配置
DEBUG = True