#!/usr/bin/env python
# -*- coding: utf8 -*-
import hashlib

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
import time

# 继承自UserMixin
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    avatar_hash = db.Column(db.String(32))

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if self.username is not None and self.avatar_hash is None:
            self.avatar_hash = hashlib.md5(self.username.encode('utf-8')).hexdigest()

    @staticmethod
    def insert_admin(username, password):
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        if password is None:
            return False
        return check_password_hash(self.password_hash, password)

    def gravatar(self, size=40, default='identicon', rating='g'):
        # if request.is_secure:
        #     url = 'https://secure.gravatar.com/avatar'
        # else:
        #     url = 'http://www.gravatar.com/avatar'
        url = 'http://www.gravatar.com/avatar'
        hash = self.avatar_hash or hashlib.md5(self.username.encode('utf-8')).hexdigest()
        return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
            url=url, hash=hash, size=size, default=default, rating=rating)


# Flask-Login要求实现一个回调函数,使用 get_id()方法返回的唯一标识用户的Unicode字符串 作为参数 返回这个用户对象
# 这个callback函数用于reload User object，根据session中存储的user id
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(50))