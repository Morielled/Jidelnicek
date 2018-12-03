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

from jidelnicek.models import Recepty, Ingredience


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
# snaha o 5 ruznych randon receptu
		nazev1 = Recepty.query.order_by(func.random()).first()
		nazev2 = Recepty.query.order_by(func.random()).first()
		nazev3 = Recepty.query.order_by(func.random()).first()
		nazev4 = Recepty.query.order_by(func.random()).first()
		nazev5 = Recepty.query.order_by(func.random()).first()
		
		if nazev1:
				return render_template('jidelnicek2.html', nazev1=nazev1)
		elif nazev2:
				return render_template('jidelnicek2.html', nazev2=nazev2)
		elif nazev3:
				return render_template('jidelnicek2.html', nazev3=nazev3)
		elif nazev4:
				return render_template('jidelnicek2.html', nazev4=nazev4)
		elif nazev5:
				return render_template('jidelnicek2.html', nazev5=nazev5)
		else:
				return render_template('jidelnicek2.html', nazev1=nazev1)


''' nahrani ingredienci k receptu

@app.route('/jidelnicek_plan')
def jidelnicek_plan():
		nazev = Recepty.query.order_by(func.random()).first()

		#ingre = Ingredience.query.filter_by(recepty_id = nazev.id).all()
		ingre = db.session.query(Recepty, Ingredience)\
														.join(Ingredience, Ingredience.recepty_id == Recepty.id).all()
		if nazev.id == ingre:
					return render_template('jidelnicek2.html', ingre=ingre)
		else:
					return render_template('jidelnicek2.html', nazev=nazev)
'''

#my_ingredience.recepty

#nove generovani receptu
@app.route('/jidelnicek_plan_new')
def jidelnicek_plan_new():
		nazev = Recepty.query.order_by(func.random()).first()
		return render_template('jidelnicek2.html', nazev=nazev)



@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404