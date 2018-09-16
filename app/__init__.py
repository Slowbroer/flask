#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from config import Config
import logging.config
from flask_cache import Cache

db = SQLAlchemy()
login_manager = LoginManager()
# 可以设置None,'basic','strong'  以提供不同的安全等级,一般设置strong,如果发现异常会登出用户
login_manager.session_protection = 'strong'
# 登陆界面的路由
login_manager.login_view = 'auth.login'
cache = Cache()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # SQLAlchemy、CSRF、Bootstrap和moment(日期处理)等的配置都写到同一个文件
    Config.init_app(app)
    CSRFProtect(app)
    db.init_app(app)
    login_manager.init_app(app)
    cache.init_app(app, config=Config.redis_cache)  # 启用缓存

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint,url_prefix='/main')


    return app