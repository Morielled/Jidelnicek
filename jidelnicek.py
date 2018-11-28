import os
#from forms import ?
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

###################################
### SQL DATABASE SECTION ###

#directory where we put the database
basedir = os.path.abspath(os.path.dirname(__file__))

#sets up the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')

#does not track all the modifications in the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

########################
### MODELS ###

#creating model (=table)
class Jidelnicek(db.Model):
			#overriding the default set up of database name
			__tablename__ = "jidelnicek"
			id = db.Column(db.Integer,primary_key=True)
			URL = db.Column(db.Text)
			title = db.Column(db.Text)
			foto = db.Column(db.Text)
			ingredience = db.Column(db.Text)
			nazev_ingredience = db.Column(db.Text)

##Neni nutne mit napsane
			def _init_(self,URL,title,foto,ingredience,nazev_ingredience):
					super.__init__(self)

					self.name = name
					self.URL = url
					self.title = title
					self.foto = foto
					self.ingredience = ingredience
					self.nazev_ingredience = nazev_ingredience

			def __repr__(self):
				#	return ??

jidelnicek = Jidelnicek("...")

