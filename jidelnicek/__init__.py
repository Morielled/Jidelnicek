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
		nazev1 = Recepty.query.order_by(func.random()).first()
		nazev2 = Recepty.query.order_by(func.random()).first()
		nazev3 = Recepty.query.order_by(func.random()).first()
		nazev4 = Recepty.query.order_by(func.random()).first()
		nazev5 = Recepty.query.order_by(func.random()).first()

		#neopakovat recepty, dodelat
		if nazev1 == nazev2:
			nazev2 == Recepty.query.order_by(func.random()).first()
			if nazev2 == nazev3:
					nazev3 == Recepty.query.order_by(func.random()).first()
					if nazev3 == nazev4:
							nazev4 == Recepty.query.order_by(func.random()).first()
							if nazev4 == nazev5:
									nazev5 == Recepty.query.order_by(func.random()).first()

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

		form1 = IngreForm1()
		
		session['nazev1.id'] = nazev1.id
		session['nazev2.id'] = nazev2.id
		session['nazev3.id'] = nazev3.id
		session['nazev4.id'] = nazev4.id
		session['nazev5.id'] = nazev5.id
	
#		if 'nazev1.id' in session:		
#			nazev1.id = session ['nazev1.id']
#		elif 'nazev2' in session:
#			nazev2 = session ['nazev2']
#		elif 'nazev3' in session:
#			nazev3 = session ['nazev3']
#		elif 'nazev4' in session:
#			nazev4 = session ['nazev4']
#		elif 'nazev5' in session:
#			nazev5 = session ['nazev5'] 
#		if request.method == 'POST':		
		if form1.validate_on_submit():
#					session['checkbox1'] = form1.checkbox1.data('checkbox1')
#						if session.get('checkbox1') == True:
						
#								return render_template('jidelnicek3.html')
				return redirect(url_for('jidelnicek_plan_seznam'))
#						
			
		else:
				return render_template('jidelnicek2.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41, ingre51=ingre51,form1=form1) #form2=form2)


	#	form1 = IngreForm1()
	#	if form1.validate_on_submit():
	#			session['checkbox1'] = form1.checkbox1.data
		#		if session.get('checkbox') == True:
		#				 	return render_template('jidelnicek3.html')

	#			return redirect(url_for('jidelnicek_plan_seznam'))
		
	#	form2 = IngreForm2()
	#	if form2.validate_on_submit():
	#			session['checkbox2'] = form2.checkbox2.data
		#		if session.get('checkbox') == True:
		#				 	return render_template('jidelnicek3.html')

	#			return redirect(url_for('jidelnicek_plan_seznam'))



#vygenerovani nakupniho seznamu
@app.route('/jidelnicek_plan_seznam', methods=['GET', 'POST'])
def jidelnicek_plan_seznam():
		# 5 ruznych random receptu

		nazev1 = session.get('nazev1.id')
		nazev2 = session.get('nazev2.id')
		nazev3 = session.get('nazev3')
		nazev4 = session.get('nazev4')
		nazev5 = session.get('nazev5')

#		if request.form.get('check_ingre'):
#			return render_template('jidelnicek3.html', ingre11=ingre11, ingre21=ingre21, ingre31=ingre31,
#		 					ingre41=ingre41, ingre51=ingre51) 
#		else: #vytvorit jidelnicek4 a do nej napsat nemate zadne polozky v nakupnim seznamu, nebo flash message
#				return render_template('jidelnicek3.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3,
#				nazev4=nazev4, nazev5=nazev5, ingre11=ingre11, ingre21=ingre21, ingre31=ingre31, ingre41=ingre41,
#				ingre51=ingre51)

		return render_template('jidelnicek3.html', nazev1=nazev1, nazev2=nazev2, nazev3=nazev3, nazev4=nazev4, nazev5=nazev5)


@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404