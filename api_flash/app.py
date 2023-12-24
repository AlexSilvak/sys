from flask import Flask, jsonify
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask import Flask,request,jsonify
from flask_cors import CORS,cross_origin
from dotenv import load_dotenv
import os 
import psycopg2
from dotenv import load_dotenv
from flask import Flask

import psycopg2
from config import config

load_dotenv()

app = Flask(__name__)

#!/usr/bin/python
import psycopg2
from config import config






cors = CORS(app, resources={r"/": {"origins": "*"}})
CORS(app, support_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)  # Adicione esta linha para habilitar CORS
# Restante do código...
CORS(app, origins=["http://localhost:5173/"])

CREATE_TABLE=("create table if not exists usuarios(id,serial primary key, name TEXT)")

# Rotas 
@app.route('/login',methods=['GET'])
def login():
    return jsonify({'message': 'Bem Vindo a API do Flask'})


@app.route('/home',methods=['GET'])
def home():

    return jsonify({'message':'Bem vindo a tela  Home'})


@app.route('/usuarios',methods=['GET'])
def usuarios():
  
  return jsonify({'message': 'Bem Vindo a API de Usuários'})

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # create a cursor
        cur = conn.cursor()
        
	# execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT * from users')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)
       
	# close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

   
if __name__ == '__main__':

    connect()
    app.run(debug=True)