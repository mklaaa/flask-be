import os
from flask import Flask,json,jsonify,request

def create_app():
  app=Flask(__name__)

  DATABASE = os.path.join(app.instance_path,'contacts.json')
  data=json.load(open(DATABASE))

  @app.route('/')
  def main():
    print('Main')
    return 'Main page'

  @app.route('/hello')
  def hello():
    print('Hey you')
    return 'Hello, World'

  return app