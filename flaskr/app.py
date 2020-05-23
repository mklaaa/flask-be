import os
from flask import Flask,jsonify,json,request

app=Flask('__name__')

SITE_ROOT=os.path.realpath(os.path.dirname(__file__))
json_url=os.path.join(SITE_ROOT,'contacts.json')
data=json.load(open(json_url))

@app.route('/')
def index():
    return 'Index page'

@app.route('/home')
def home():
    return jsonify(data)

@app.route('/login', methods=['GET','POST'])
def login():
    user = request.form.get('user')
    print(user)
    pwd= request.form.get('pwd')
    print(pwd)
    return user