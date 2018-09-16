#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_script import Manager,Shell
from flask_migrate import Migrate,MigrateCommand

from app import create_app, db
from app.model import User

app = create_app()
manager = Manager(app)
migrate = Migrate(app,db)


if __name__ == '__main__':
    manager.run()

