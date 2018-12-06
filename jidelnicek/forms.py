from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, SubmitField

class IngreForm1(FlaskForm):

#			checkbox1 = BooleanField()
			submit1 = SubmitField('Mám hotovo! Chci vidět nákupní seznam')

class IngreForm2(FlaskForm):

			checkbox2 = BooleanField()
			submit2 = SubmitField('Mám hotovo! Chci vidět nákupní seznam')