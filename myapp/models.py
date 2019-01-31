#!/usr/bin/env python2
#coding:utf-8

import pymongo


class DBmanager(object):
    def __init__(self, dbname):
        connection = pymongo.MongoClient()
        self.connection = connection
        self._connect_db(dbname=dbname)

    def _connect_db(self, dbname):
        tdb = self.connection.MS_pipe
        self.post_info = tdb[dbname]

    def insert_one(self, info):
        self.post_info.insert_one(info)

    def find_one(self, info):
        return self.post_info.find_one(info)

    def find(self, info=""):
        return self.post_info.find(info)

    def update_one(self, pattern, newinfo, upsert=True):
        self.post_info.update_one(pattern, newinfo, upsert)

    def delete_one(self, info):
        self.post_info.delete_one(info)

    def delete_many(self, info):
        self.post_info.delete_many(info)

    def drop(self):
        self.post_info.drop()
        return "Drop current databse!"

    def _close(self):
        self.connection.close()


