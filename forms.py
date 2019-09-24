from flask import Flask
from flask_wtf import Form, FlaskForm
from wtforms import Form, SubmitField, BooleanField, StringField, PasswordField, validators, SelectField, RadioField
from wtforms.fields.html5 import EmailField
"""
Util forms for Facesmash

made by suulcoder
"""

class DATA(Form):#Form for principal information
	name =  StringField('Nombre',[validators.DataRequired(message='Campo Requerido')])#Validate
	mail = EmailField('E-mail',[validators.DataRequired(message='Escriba un E-mail Valido')])#Validate mail
	accept = BooleanField('Acepto Terminos y Condiciones', [validators.DataRequired(message='Campo Requerido')])
	gender = RadioField('Genero', choices=[('H','Hombre'),('M','Mujer')])
	career =  StringField('Career',[validators.DataRequired(message='Campo Requerido')])#Validate
	submit = SubmitField('Ingresar')