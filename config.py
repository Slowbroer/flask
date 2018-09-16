#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import os


class Config():
    DEBUG_HOST_NAMES = ['tanglihao-PC', 'AJBC-1498']
    MASTER_HOST_NAME = 'jiangzhiming-virtual-machine'
    HOST_NAME = socket.gethostname()
    IS_MASTER_SERVER = [False, True][HOST_NAME == MASTER_HOST_NAME]
    # APP_ID = "hnQkj87tQa9ROpNRAa"
    # APP_SECRET = 'k5MD91gW0ry6diME3OPBkOXjLzZYxv38'
    # AGENT_ID = 'agRjzP4FXpQrwRWaZN'

    # APP_ID = 'hnZrRdoHJ1BqJG3dDm'
    # APP_SECRET = 'B0e9k5wjzr2K4UJbNEJz7YXxd2EloNmJ'
    # AGENT_ID = 'aglBmVDc3XJe0gA1jW'

    APP_ID = ''
    APP_SECRET = ''
    AGENT_ID = ''
    ERWEIMA_ADDR = ""

    if not IS_MASTER_SERVER:
        DEBUG = True
        SQLALCHEMY_TRACK_MODIFICATIONS = True
        SQLALCHEMY_COMMIT_ON_TEARDOWN = True
        SQLALCHEMY_RECORD_QUERIES = True
        # SQLALCHEMY_DATABASE_URI = 'mysql://root:lihao@localhost:3306/blog_mini?charset=utf8'
        SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/haina?charset=utf8'
        if HOST_NAME == DEBUG_HOST_NAMES[1]:
            SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost:3306/haina?charset=utf8'
            APP_ID = "hnRkK6aU07o6PQBWrQ"
            APP_SECRET = '9Mb4jlq7ZQg6GUDO4EWxZZXWekw6AYPO'
            AGENT_ID = 'agejMNvsxKNybwLbkX'
            ERWEIMA_ADDR = 'aaaa'

        # 添加本地配置
        if os.path.exists('./local.conf'):
            file_object = open('./local.conf')
            try:
                config_list = file_object.readlines()
                if config_list[0] == 'liuhengdong\n':
                    SQLALCHEMY_DATABASE_URI = config_list[1]
            finally:
                file_object.close()

        SECRET_KEY = '\x19\x94?>\xc3\'\xe2\x14c\xdb9\x1e\x7f\xc4\x15\x9a\xd2V\x0b\xe9NSk"'
        WTF_CSRF_SECRET_KEY = '\x19\x94?>\xc3\'\xe2\x14c\xdb9\x1e\x7f\xc4\x15\x9a\xd2V\x0b\xe9NSk"'  # for csrf protection
        # Take good care of 'SECRET_KEY' and 'WTF_CSRF_SECRET_KEY', if you use the
        # bootstrap extension to create a form, it is Ok to use 'SECRET_KEY',
        # but when you use tha style like '{{ form.name.labey }}:{{ form.name() }}',
        # you must do this for yourself to use the wtf, more about this, you can
        # take a reference to the book <<Flask Framework Cookbook>>.
        # But the book only have the version of English.
        # 缓存配置(Redis)
        redis_cache = {
            'CACHE_TYPE': 'redis',
            'CACHE_KEY_PREFIX': '',
            'CACHE_REDIS_HOST': '58.249.57.254',
            'CACHE_REDIS_PORT': 6389,
            'CACHE_REDIS_DB': '0',
            'CACHE_REDIS_PASSWORD': 'redis*&ajbhaina'
        }
    else:
        DEBUG = False
        SQLALCHEMY_TRACK_MODIFICATIONS = True
        SQLALCHEMY_COMMIT_ON_TEARDOWN = True
        SQLALCHEMY_RECORD_QUERIES = True
        # SQLALCHEMY_DATABASE_URI = 'mysql://root:lihao@localhost:3306/blog_mini?charset=utf8'
        # SQLALCHEMY_DATABASE_URI = 'mysql://ajb:ajb.300155@localhost:3306/haina?charset=utf8'
        SQLALCHEMY_DATABASE_URI = 'mysql://root:anjubao@58.249.57.254:3306/platform?charset=utf8'

        SECRET_KEY = '\x19\x94?>\xc3\'\xe2\x14c\xdb9\x1e\x7f\xc4\x15\x9a\xd2V\x0b\xe9NSk"'
        WTF_CSRF_SECRET_KEY = '\x19\x94?>\xc3\'\xe2\x14c\xdb9\x1e\x7f\xc4\x15\x9a\xd2V\x0b\xe9NSk"'  # for csrf protection
        # 缓存配置(Redis)
        redis_cache = {
            'CACHE_TYPE': 'redis',
            'CACHE_KEY_PREFIX': '',
            'CACHE_REDIS_HOST': '127.0.0.1',
            'CACHE_REDIS_PORT': 6389,
            'CACHE_REDIS_DB': '1',
            'CACHE_REDIS_PASSWORD': 'redis*&ajbhaina'
        }

    @staticmethod
    def init_app(app):
        pass