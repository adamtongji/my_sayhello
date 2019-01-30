#!/usr/bin/env python2
#coding:utf-8

from flask import Flask, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
# from myapp.models import DBmanager
from flask_pymongo import PyMongo

app =Flask('myapp')
app.config.from_pyfile("settings.py")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

usrdb = PyMongo(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from myapp import views, errors, commands

