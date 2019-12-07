from flask import Flask, jsonify, request

app = Flask(__name__)
cred = [{'username':'B'}]
@app.route('/', methods=['GET'])
def index():
    return 'Test'


@app.route('/auth', methods=['GET', 'POST'])
def recCredential():

    #creds = {'username' : request.json['username']}
    #cred.append(creds)
    return request.json['username'] #jsonify({'cred': creds})