import os
from flask import Flask, render_template, url_for, jsonify
from flask_cachebuster import CacheBuster

app = Flask(__name__, template_folder='templates', static_folder='assets')
config = { 'extensions': ['.js', '.css', '.csv'], 'hash_size': 5 }


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/page")
def page():
    """ Test payload """ 
    data = {
        'id': 1,
        'date': '0000-00-00',
        'username': 'anonymous',
        'title': 'test page title',
        'name': 'journal name test',
        'content': 'test data content'
    }
    return jsonify(data)


@app.route("/login", methods=('GET', 'POST'))
def login():
    return render_template('login.html')


@app.route("/register", methods=('GET', 'POST'))
def register():
    return render_template('register.html')


if __name__ == '__main__':
    cache_buster = CacheBuster(config=config)
    cache_buster.init_app(app)
    app.run(debug = True)
