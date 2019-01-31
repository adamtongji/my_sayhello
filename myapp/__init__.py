#!/usr/bin/env python2
#coding:utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from myapp.models import DBmanager
from myapp.settings import MONGO_DBNAME

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

mongo = DBmanager(dbname=MONGO_DBNAME)


from myapp import views, errors, commands

