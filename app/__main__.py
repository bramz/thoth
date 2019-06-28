import os
import sqlite3
import datetime
import base64
from flask import Flask, render_template, session
from flask import jsonify, request, g, redirect, url_for
from flask_cachebuster import CacheBuster
from flask_login import LoginManager, UserMixin, login_user, logout_user


"""  Application management """
app = Flask(__name__, template_folder='templates', static_folder='assets')
app.secret_key = b'|\xcc\x96\x0f]:\xd0;|\'' # Generate a new key and keep this secret
config = { 'extensions': ['.js', '.css', '.csv'], 'hash_size': 5 }
db = '/home/wired/wired/thoth/db/thoth.db' # Path to database
now = datetime.datetime.now()


""" Database management """
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


""" Index route """
@app.route("/")
def index():
    if not session.get('logged_in'):
        return render_template('index.html')

    return render_template('index.html', user=user_loader(session['username']))


""" Page route /page - outputs data for particular page """
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


""" Entries route - list entries for user """
@app.route("/entries")
def entries():
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


""" Entry route - create an entry """
@app.route("/entry", methods=('GET', 'POST'))
def entry():
    if request.method == 'POST':
        with app.app_context():
            stmt = 'insert into journal ' \
                '(date, user, title, name, content) ' \
                'values(?, ?, ?, ?, ?)'
    
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
            c.cursor().close()
            print("Commited entry to db.")

    return render_template('entry.html')


"""  User/Login management """
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class User(UserMixin):
    def __init__(self, id: int, username: str, password: str):
        self.data = {
            'id': id,
            'username': username,
            'password': password
        }
        
    def get_user(self) -> dict:
        return self.data


@login_manager.user_loader
def user_loader(username: str):
    with app.app_context():
        stmt = 'select * from user where username = ?'
        c = get_db()
        cur = c.cursor().execute(stmt, (username,))
        u = cur.fetchall()
        cur.close()

    if username == u[0][1]:
            user = User(u[0][0], u[0][1], u[0][2])

    return user.get_user()


@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')

    if authenticate_user(
        request.json['username'], 
        request.json['password']
    ) is True:
        user_loader(request.json['username'])
        session['logged_in'] = True
    return "success"


@app.route("/logout")
def logout():
    logout_user()
    return redirect('/')


@app.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        with app.app_context():
            stmt = 'insert into user (username, password, active) values (?, ?, ?)'

            c = get_db()
            c.cursor().execute(
                stmt,
                (
                    request.json['username'],
                    request.json['password'],
                    request.json['active'],
                )
            )
            c.commit()
            c.cursor().close()

            session['username'] == request.json['username']
            return "success"

    return render_template('register.html')


def authenticate_user(username: str, password: str) -> bool:
    with app.app_context():
        stmt = "select password from user where username = ?"
        c = get_db()
        cur = c.cursor().execute(stmt, (username,))
        pw = cur.fetchone()

        if password == pw[0]:
            return True

    return False


""" Main application """
if __name__ == '__main__':
    cache_buster = CacheBuster(config=config)
    cache_buster.init_app(app)
    app.run(debug = True)
