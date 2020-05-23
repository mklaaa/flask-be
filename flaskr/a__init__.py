import os
from flask import Flask, json, jsonify, request


def create_app():
    app = Flask(__name__)

    DATABASE = os.path.join(app.instance_path, 'contacts.json')
    data = json.load(open(DATABASE))

    @app.route('/')
    def main():
        print('Main')
        return 'Main page'

    @app.route('/home')
    def home():
        print('Home')
        return jsonify(data)

    @app.route('/login')
    def login():
        user = request.args.get('user')
        pwd = request.args.get('pwd')
        print(user)
        print(pwd)

        return 'login'

    @app.route('/contact')
    def contact():
        print('Contact')

        foo = {'m': {'a': 10}, 'n': {'a': 20}}
        result=[d for d in data.values()]

        print(result)

        return '_filtered'

    return app
