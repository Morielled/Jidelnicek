import os
from flask import Flask, session, request, redirect, make_response
from flask import render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func, select
from sqlalchemy.orm import sessionmaker

from jidelnicek.forms import IngreForm1, IngreForm2
#import pdfkit

app = Flask (__name__)

#configuration for the forms
app.config['SECRET_KEY'] = 'development'

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


from jidelnicek.models import Recepty, Ingredience


###############################
###### ROUTES #################
###############################

@app.route('/')
def index():
		return render_template('index.html')

#prozatim schovat, nez budou filtry
#@app.route('/jidelnicek')
#def jidelnicek():
#		return render_template('jidelnicek.html')


@app.route('/jidelnicek_plan', methods=['GET', 'POST'])
def jidelnicek_plan():
		# 5 ruznych random receptu

	form1 = IngreForm1()

	recept1 = Recepty.query.order_by(func.random()).first()
	recept2 = Recepty.query.order_by(func.random()).first()
	recept3 = Recepty.query.order_by(func.random()).first()
	recept4 = Recepty.query.order_by(func.random()).first()
	recept5 = Recepty.query.order_by(func.random()).first()
	
	session ["recept1id"] = recept1.id
	session ["recept2id"] = recept2.id
	session ["recept3id"] = recept3.id
	session ["recept4id"] = recept4.id
	session ["recept5id"] = recept5.id

	#zahrnuti ingredienci do receptu	
	ingre1 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = recept1.id).all()
	ingre2 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = recept2.id).all()
	ingre3 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = recept3.id).all()
	ingre4 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = recept4.id).all()
	ingre5 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = recept5.id).all()

	ingre11 = [item[0] for item in ingre1]
	ingre21 = [item[0] for item in ingre2]
	ingre31 = [item[0] for item in ingre3]
	ingre41 = [item[0] for item in ingre4]
	ingre51 = [item[0] for item in ingre5]

	return render_template('jidelnicek2.html', recept1=recept1, recept2=recept2, recept3=recept3, recept4=recept4, recept5=recept5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41, ingre51=ingre51, form1=form1)




#vygenerovani nakupniho seznamu
@app.route('/jidelnicek_plan_seznam', methods=['GET', 'POST'])
def jidelnicek_plan_seznam():
		
		form1 = IngreForm1()
	
		form1id = request.form['recept1id']
		form2id = request.form['recept2id']
		form3id = request.form['recept3id']
		form4id = request.form['recept4id']
		form5id = request.form['recept5id']

		recept1 = db.session.query(Recepty).filter_by(id = form1id).first()
		recept2 = db.session.query(Recepty).filter_by(id = form2id).first()
		recept3 = db.session.query(Recepty).filter_by(id = form3id).first()
		recept4 = db.session.query(Recepty).filter_by(id = form4id).first()
		recept5 = db.session.query(Recepty).filter_by(id = form5id).first()
		
		ingre1 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = form1id).all()
		ingre2 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = form2id).all()
		ingre3 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = form3id).all()
		ingre4 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = form4id).all()
		ingre5 = db.session.query(Ingredience.ingredience).filter_by(recepty_id = form5id).all()

		ingre11 = [item[0] for item in ingre1]
		ingre21 = [item[0] for item in ingre2]
		ingre31 = [item[0] for item in ingre3]
		ingre41 = [item[0] for item in ingre4]
		ingre51 = [item[0] for item in ingre5]

	
		formingred1 = request.form['ingred1']
		
		formingred11 = [item for item in formingred1]

		return render_template('jidelnicek3.html', recept1=recept1, recept2=recept2, recept3=recept3, recept4=recept4, recept5=recept5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41, ingre51=ingre51, form1=form1, form1id=form1id) #, formingred11=formingred11)


@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404