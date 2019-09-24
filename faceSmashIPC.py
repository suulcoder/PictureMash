"""
Welcome everybody to my code
here will be a simple code 
for FaceSmash, but it will use 
art work, arquitecture and logotipes
to be qualified. 

Made by Saul Contreras (SuulCoder)
"""
#We import all important libraries. 
from flask import *
from flask_wtf import CsrfProtect
import forms
import json
from config import DevelopmentConfig
import pymongo

conexion = pymongo.MongoClient()#Database Conection
db = conexion.Data
coleccion = db.Usuarios
app = Flask(__name__)#Instantiate Flask
app.config.from_object(DevelopmentConfig)

@app.route('/', methods=['GET','POST'])#For routes and forms
def index():#Index. Home Page
	form = forms.DATA(request.form)#Instate forms
	userdb = {}
	if request.method == 'POST' and form.submit.data and form.validate():#Evaluate if the form has data
		userdb['Name']=form.name.data
		userdb['Mail']=form.mail.data
		userdb['Career']=form.career.data
		userdb['Gender']=form.gender.data
		db.data.insert(userdb)#Insertamos los comentarios
		i = form.mail.data
		flash('Gracias')#Thank the user
		return redirect('user/'+i)
	return render_template('Home.html', form=form)#Call the function

@app.route('/user/<usuario>', methods=['GET','POST'])
def user(usuario):#Index de URL
	datos = coleccion.find({'email':usuario})
	if request.method == 'POST':#Si se envian datos
		#Do nothing yet because here is going to be the random choice
	elif request.method == 'GET':
		return render_template('user.html')	

