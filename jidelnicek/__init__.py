import os
from flask import Flask
from flask import render_template,url_for
#from flask_migrate import Migrate

app = Flask (__name__)

#configuration for the forms
#app.config['SECRET_KEY'] = 'mysecretkey'

###################################
### MODELS SET UP #################
###################################

#directory where we put the database

#sets up the database location

#does not track all the modifications in the database

#Migrate(app,db)

###############################
###### ROUTES #################

@app.route('/')
def index():
		return render_template('index.html')

@app.route('/jidelnicek')
def jidelnicek():
		return render_template('jidelnicek.html')

@app.route('/jidelnicek2')
def jidel_planovac():

		#recept = Jidelnicek.query.limit(5).all()

@app.errorhandler(404)
def error_404(error):
		return render_template('error_pages/404.html'), 404