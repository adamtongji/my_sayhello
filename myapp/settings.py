#!/usr/bin/env python2
#coding:utf-8

import os

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'testdb'
SECRET_KEY = os.getenv('SECRET_KEY', 'secret string')
