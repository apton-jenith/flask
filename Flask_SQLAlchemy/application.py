from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__) #creating flask object

app.config.from_pyfile('config.cfg') #connecting the configuration file

db = SQLAlchemy(app) #initialise the database object

class Test(db.Model): # name of the table will be Test, db.Model - injects the SQLAlchemy functionality into the class
	id = db.Column(db.Integer, primary_key=True) #id is the column and db. Integer represents the datatype

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(30),unique=True)
	password = db.Column(db.String(30))
	email = db.Column(db.String(50))
	join_date = db.Column(db.DateTime)

	orders = db.relationship('Order', backref='member', lazy = 'dynamic')

	def __repr__(self): # returns a representation of object in the database
		return '<Member %r>' % self.username

class Order(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	price = db.Column(db.Integer)
	member_id = db.Column(db.Integer,db.ForeignKey('member.id'))


if __name__ == '__main__': #run the application in main
	app.run()