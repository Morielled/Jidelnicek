import os
from flask import Flask, session, request
from flask import render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
#from flask_migrate import Migrate

app = Flask (__name__)

#configuration for the forms
app.config['SECRET_KEY'] = 'mysecretkey'

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
		ingre2 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev2.id).all()
		ingre3 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev3.id).all()
		ingre4 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev4.id).all()
		ingre5 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev5.id).all()

		ingre11 = [item[0] for item in ingre1]
		ingre21 = [item[0] for item in ingre2]
		ingre31 = [item[0] for item in ingre3]
		ingre41 = [item[0] for item in ingre4]
		ingre51 = [item[0] for item in ingre5]
		
		return render_template('jidelnicek2.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41, ingre51=ingre51)


#nove generovani receptu
@app.route('/jidelnicek_plan_new')
def jidelnicek_plan_new():
		# 5 ruznych random receptu
		nazev1 = Recepty.query.order_by(func.random()).first()
		nazev2 = Recepty.query.order_by(func.random()).first()
		nazev3 = Recepty.query.order_by(func.random()).first()
		nazev4 = Recepty.query.order_by(func.random()).first()
		nazev5 = Recepty.query.order_by(func.random()).first()
		
		#zahrnuti ingredienci do receptu
		ingre1 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev1.id).all()
		ingre2 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev2.id).all()
		ingre3 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev3.id).all()
		ingre4 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev4.id).all()
		ingre5 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev5.id).all()

		ingre11 = [item[0] for item in ingre1]
		ingre21 = [item[0] for item in ingre2]
		ingre31 = [item[0] for item in ingre3]
		ingre41 = [item[0] for item in ingre4]
		ingre51 = [item[0] for item in ingre5]
		
		return render_template('jidelnicek2.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41, ingre51=ingre51)

#vygenerovani nakupniho seznamu
@app.route('/jidelnicek_plan_seznam')
def jidelnicek_plan_seznam():
		nazev1 = Recepty.query.order_by(func.random()).first()
		nazev2 = Recepty.query.order_by(func.random()).first()
		nazev3 = Recepty.query.order_by(func.random()).first()
		nazev4 = Recepty.query.order_by(func.random()).first()
		nazev5 = Recepty.query.order_by(func.random()).first()

		ingre1 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev1.id).all()
		ingre2 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev2.id).all()
		ingre3 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev3.id).all()
		ingre4 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev4.id).all()
		ingre5 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = nazev5.id).all()
	
		ingre11 = [item[0] for item in ingre1]
		ingre21 = [item[0] for item in ingre2]
		ingre31 = [item[0] for item in ingre3]
		ingre41 = [item[0] for item in ingre4]
		ingre51 = [item[0] for item in ingre5]

	#	if request.form.get('check_ingre'):
		#	return render_template('jidelnicek3.html', ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, #ingre41=ingre41, ingre51=ingre51) 

		return render_template('jidelnicek3.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41, ingre51=ingre51)


@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404