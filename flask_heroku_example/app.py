import os
import psycopg2
from flask import Flask, render_template, , jsonify, request, g


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
 #    return "Hello Krsna"   
     
     
app = Flask(__name__)
cred = [{'username':'B'}]
@app.route('/', methods=['GET'])
def index():
    return 'Test'


@app.route('/auth', methods=['GET', 'POST'])
def recCredential():

    #creds = {'username' : request.json['username']}

  
    #cred.append(creds)
    return request.json['username'] #jsonify({'cred': c
    # reds})