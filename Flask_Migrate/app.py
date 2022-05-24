from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import mysql.connector
import pymysql


db = SQLAlchemy()
migrate = Migrate()

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))


class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    total = db.column(db.Integer)


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Current-Root-Password@localhost/test1'
    db.init_app(app)
    migrate.init_app(app,db)


    return app

