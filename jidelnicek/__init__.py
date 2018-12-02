import os
from flask import Flask
from flask import render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
#from flask_migrate import Migrate

app = Flask (__name__)

#configuration for the forms
#app.config['SECRET_KEY'] = 'mysecretkey'

###################################
### MODELS SET UP #################
###################################

#directory where we put the database
basedir = os.path.abspath(os.path.dirname(__file__))

#sets up the database location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'jidelnicek.db')

#does not track all the modifications in the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#Migrate(app,db)

from jidelnicek.models import Recepty, Tagy, Ingredience

###############################
###### ROUTES #################
###############################

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/jidelnicek')
def jidelnicek():
		return render_template('jidelnicek.html')

@app.route('/jidelnicek_plan')
def jidelnicek_plan():
		nazev = Recepty.query.order_by(func.random()).first()
		return render_template('jidelnicek2.html', nazev=nazev)



#nove generovani receptu
@app.route('/jidelnicek_plan_new')
def jidelnicek_plan_new():
		nazev = Recepty.query.order_by(func.random()).first()
		return render_template('jidelnicek2.html', nazev=nazev)


'''	ingredience = Recepty.query.order_by(func.random()).first()
		return render_template('jidelnicek2.html', ingredience=ingredience) '''

'''
@app.route('/jidelnicek_plan')
def jidelnicek_plan():

		nazev = Recepty.query.order_by(func.rand()).first()
		#nazev = session.query(Recepty).order_by(func.rand()).limit(1)
						#return render_template('jidelnicek2.html', nazev=nazev)
		#select.order_by(func.random()).limit(1)
		recept = Recepty.query.limit(1).all()
		#vypis ingredienci
		#ingredience = Ingredience.ingredience.query.all()
		return render_template('jidelnicek2.html', recept=recept) '''

@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404