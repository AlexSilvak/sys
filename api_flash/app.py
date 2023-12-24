from flask import Flask, jsonify
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
from flask_cors import CORS  # Importe a extensão
import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func

from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:sysdba23@localhost:5432/helpdesk")


args, kwargs = engine.dialect.create_connect_args(engine.url)
args, kwargs

print(args, kwargs)





app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
CORS(app, support_credentials=True)

app.config['CORS_HEADERS'] = 'Content-Type'


CORS(app)  # Adicione esta linha para habilitar CORS
# Restante do código...
CORS(app, origins=["http://localhost:5173/"])



# Rotas 
@app.route('/login',methods=['GET'])
def login():
    return jsonify({'message': 'Bem Vindo a API do Flask'})


@app.route('/home',methods=['GET'])
def home():

    return jsonify({'message':'Bem vindo a tela  Home'})


@app.route('/usuarios',methods=['GET'])
def usuarios():
    return jsonify({'message':'Bem vindo a tela de Usuarios'})

if __name__ == '__main__':
    app.run(debug=True)
