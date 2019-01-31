#!/usr/bin/env python2
#coding:utf-8
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class MyForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(1, 20)])
    body = TextAreaField("Message", validators=[DataRequired(), Length(1, 200)])
    submit = SubmitField()

