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
# 5 ruznych random receptu
		nazev1 = Recepty.query.order_by(func.random()).first()
		nazev2 = Recepty.query.order_by(func.random()).first()
		nazev3 = Recepty.query.order_by(func.random()).first()
		nazev4 = Recepty.query.order_by(func.random()).first()
		nazev5 = Recepty.query.order_by(func.random()).first()
		
		#zahrnuti ingredienci do receptu
		ingre1 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev1.id).all()
		ingre2 = Ingredience.query.filter_by(recepty_id = nazev2.id).all()
		ingre3 = Ingredience.query.filter_by(recepty_id = nazev3.id).all()
		ingre4 = Ingredience.query.filter_by(recepty_id = nazev4.id).all()
		ingre5 = Ingredience.query.filter_by(recepty_id = nazev5.id).all()

		return render_template('jidelnicek2.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5, ingre1=ingre1, ingre2=ingre2, ingre3=ingre3, ingre4=ingre4, ingre5=ingre5)

''' dalsi pokus o random
@app.route('/jidelnicek_plan')
def jidelnicek_plan():
		
		nazev = Recepty.query.options(load_only('id')).offset(
            func.floor(
                func.random() *
                db.session.query(func.count(Recepty.id))
            )
        		).limit(1).all() 
    return render_template('jidelnicek2.html', nazev=nazev)
'''

'''
@app.route('/jidelnicek_plan')
def jidelnicek_plan():
		nazev = Recepty.query.order_by(func.random()).first()
#zahrnuti ingredienci do receptu
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
		nazev1 = Recepty.query.order_by(func.random()).first()
		nazev2 = Recepty.query.order_by(func.random()).first()
		nazev3 = Recepty.query.order_by(func.random()).first()
		nazev4 = Recepty.query.order_by(func.random()).first()
		nazev5 = Recepty.query.order_by(func.random()).first()
		
		return render_template('jidelnicek2.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5)


@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404