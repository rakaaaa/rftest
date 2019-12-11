import os
import psycopg2
from flask import Flask, render_template,jsonify, request, g
import pandas as pd
import numpy as np
from simple_salesforce import Salesforce, SalesforceLogin
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


def connect_db():
    return psycopg2.connect(os.environ.get('DATABASE_URL'))


#@app.before_request
#def before_request():
  #  g.db_conn = connect_db()


#@app.route('/')
#def index():
#    cur = g.db_conn.cursor()
 #   cur.execute("SELECT * FROM country;")
  #  return render_template('index.html', countries=cur.fetchall())
 #      return "Hello Krsna"   
     
     
app = Flask(__name__)
cred = [{'username':'B'}]
@app.route('/', methods=['GET'])
def index():
    return 'Test'


@app.route('/auth', methods=['GET', 'POST'])
def recCredential():

    #creds = {'username' : request.json['username']}

    #decoloads(request)
    #cred.append(creds)
    loginData = AuthAndRetrieveData(request.json['userName'], request.json['password'], request.json['token'], request.json['isProduction'])
    loginData.retrieveData()
    return request.json['username'] #jsonify({'cred': c
    # reds})
    
    
class AuthAndRetrieveData:
    def __init__(self, userName, password, token, isProduction):
        self.userName = userName
        self.password = password
        self.isProduction = isProduction
        self.sf = null;
        
    def authentication():
        session_id, instance = SalesforceLogin(userName, password, security_token=token, sandbox=isProduction) 
        sf = Salesforce(instance=instance, session_id=session_id)
    
    def retrieveData(self):
        queryRFA = sf.bulk.Request_for_Assistance__c.query("Select id, Name from Request_for_Assistance__c limit 10")
        
    