#!/usr/bin/env python
# -*- coding: utf8 -*-
import hashlib

from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import db, login_manager
import time

class User(UserMixin,db.Model):
    pass