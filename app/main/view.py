#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import parse
from flask import render_template, request, redirect, Flask, session, url_for
from . import main
import requests
import json
import hashlib
from app.model import User
from config import Config
import time
from app import db,cache


@main.route("/index")
def index():
    # return '111'
    return render_template("index.html",message='hello world')