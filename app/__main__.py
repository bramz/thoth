import os
import sqlite3
import datetime
from flask import Flask, render_template, jsonify, request, g
from flask_cachebuster import CacheBuster

app = Flask(__name__, template_folder='templates', static_folder='assets')
config = { 'extensions': ['.js', '.css', '.csv'], 'hash_size': 5 }
db = '../db/thoth.db'
now = datetime.datetime.now()


def get_db():
    d = getattr(g, '_database', None)
    if d is None:
        d = g._database = sqlite3.connect(db)
    return d


@app.teardown_appcontext
def close_connection(exception):
    d = getattr(g, '_database', None)
    if d is not None:
        d.close()


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


@app.route("/entry", methods=('GET', 'POST'))
def entry():
    if request.method == 'POST':
        with app.app_context():
            stmt = 'insert into journal (date, user, title, name, content) values(?, ?, ?, ?, ?)'
            c = get_db()
            c.cursor().execute(
                stmt, 
                (
                    now,
                    'anonymous',
                    request.json['title'],
                    'test journal',
                    request.json['content'],
                )
            )
            c.commit()
            print("Commited entry to db.")

    return render_template('entry.html')


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
