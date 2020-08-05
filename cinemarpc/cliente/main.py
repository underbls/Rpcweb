from flask import Flask
from flask import request
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from zeep import Client, Settings
#import bb y modulos internos:

import forms


#conect con spyne
wsdl = 'http://localhost:8000/?wsdl'
settings = Settings(strict=True,xml_huge_tree=True)
rpc_client = Client(wsdl=wsdl,settings=settings)

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/prueba.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/prueba'
#Rutas del proyectos web

#pagina principal
@app.route('/')
def hello_word():
    return render_template('index.html')



#Servicio login
@app.route('/service1',methods=['GET','POST'])
def service1():
    login_form = forms.LogForm(request.form)
    data=None
    if request.method == 'POST':
        #tomar info form y la envia
        data = rpc_client.service.log_user(login_form.name.data,login_form.passs.data)
        print(data)
    return render_template('services/index.html',form = login_form, data = data)
        #data = rpc_client.service.say_hello('tin','hhhhh')
        #return render_template('services/say_hello.html',hello_form,data)

#Servicio para obtener datos de una pelicula:
@app.route('/service3',methods=['GET','POST'])
def service3():
    list_hello_form = forms.ListHelloForm(request.form)
    myList=[]
    if request.method == 'POST':
        myList = rpc_client.service.list_hello(list_hello_form.name_movie.data,list_hello_form.date_p.data)
    return render_template('services/list_hello.html',form = list_hello_form, data = myList)


#param inicio de la app
if __name__ =='__main__':
    app.run(debug = True, host= '0.0.0.0')
