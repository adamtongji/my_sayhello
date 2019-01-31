#!/usr/bin/env python2
#coding:utf-8
import click
from myapp import app, mongo


@app.cli.command()
@click.option("--drop", is_flag=True, help="Delete all saved data")
def initdb(drop):
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?', abort=True)
        mongo.delete_many({})
        click.echo("Data all clear.")
    click.echo("Initialize database")


@app.cli.command()
@click.option("--count", default=20, help="Generate quantity of messages")
def forge_data(count):
    from faker import Faker
    fake =Faker()
    for i in range(count):
        message = {
            "name":fake.name(),
            "body":fake.sentence(),
            "timestamp":fake.date_time_this_year()
        }
        mongo.insert_one(message)
    click.echo('Add %d fake messages.' % count)
