from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, RadioField, SubmitField

class IngreForm(FlaskForm):

			checkbox = BooleanField()
			submit = SubmitField('Mám hotovo! Chci vidět nákupní seznam')