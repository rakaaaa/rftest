import os
#import psycopg2
from flask import Flask, render_template,jsonify, request, g
#import pandas as pd
#import numpy as np
from simple_salesforce import Salesforce, SalesforceLogin
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'XYZ')


#def connect_db():
#    return psycopg2.connect(os.environ.get('DATABASE_URL'))


#@app.before_request
#def before_request():
  #  g.db_conn = connect_db()


#@app.route('/')
#def index():
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

    loginData = AuthAndRetrieveData(request.json['userName'], request.json['password'], request.json['token'], request.json['isSandbox'])
    sf = loginData.authentication("Test")
    queryRFA = loginData.retrieveData(sf)
    return queryRFA #jsonify({'cred': c
    # reds})
    
    
class AuthAndRetrieveData:
    def __init__(self, userName, password, token, isSandbox):
        self.userName = userName
        self.password = password
        self.isSandbox = isSandbox 
        self.token = token
        
    def authentication(self, data):
        if(self.token):
            session_id, instance = SalesforceLogin(self.userName, self.password, security_token=self.token, sandbox=self.isSandbox ) 
        else:
            session_id, instance = SalesforceLogin(self.userName, self.password, sandbox=self.isSandbox )         
        sf = Salesforce(instance=instance, session_id=session_id)
        return sf
        
    def retrieveData(self, sf):
        queryRFA = sf.bulk.Request_for_Assistance__c.query("Select id, Name from Request_for_Assistance__c limit 10")
        return queryRFA
    