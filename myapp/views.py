#!/usr/bin/env python2
#coding:utf-8

from flask import flash, redirect, url_for, render_template

from myapp import app, mongo
from myapp.forms import MyForm
from datetime import datetime
# from myapp.models import DBmanager


@app.route('/',methods=["POST","GET"])
def index():
    messages = mongo.find({})
    mess_out = []
    for mess in messages:
        mess_out.append(mess)
    mess_out.sort(key=lambda x: x["timestamp"], reverse=True)
    form = MyForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        timestamp = datetime.utcnow()
        insert_info = {"name":name, "body":body, "timestamp":timestamp}
        mongo.insert_one(insert_info)
        flash('Your message have been sent to the our website!')
        return redirect(url_for("index"))
    return render_template("index.html", form=form, messages=mess_out)