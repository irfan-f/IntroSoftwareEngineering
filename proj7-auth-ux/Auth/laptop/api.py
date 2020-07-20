# List all Laptop Service

import os
import flask
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from flask_login import (LoginManager, current_user, login_required,
                             login_user, logout_user, UserMixin,
                             confirm_login, fresh_login_required)
from config import Config
from forms import LoginForm, RegistrationForm
from password import hash_password, verify_password
import logging
from tokenWork import generate_auth_token, verify_auth_token

import flask_wtf
from flask_wtf.csrf import CSRFProtect, CSRFError

# Create user class
class User(UserMixin):
    def __init__(self, name, id, active=True):
        self.name = name
        self.id = id
        self.active = active

    def is_active(self):
        return self.active

# Instantiate App and mongodb
app = Flask(__name__)
api = Api(app)

# Enable CSRF protection, used "https://flask-wtf.readthedocs.io/en/stable/csrf,html" for information and code
csrf = CSRFProtect(app)

@app.errorhandler(CSRFError)
def handle_csrf(e):
    return render_template('csrf.html'), 400


client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.timedb
dbpass = client.passdb

app.config.from_object(Config)

global token
token = None
# Create login_manager class and configure
login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u"Log in to access."
login_manager.refresh_view = "reauth"
login_manager.needs_refresh_message = (u"For securtiy, please reauthenticate to access.")
# User id Count
global x
x = dbpass.userdb.count()

@app.route('/ui')
def ui():
    return render_template('ui.html')

@login_manager.user_loader
def load_user(id):
    users = dbpass.userdb.find({'_id': int(id) }, {'password': 0} )
    for y in users:
        user = y
    return User(user['username'], id)

def is_safe_url(next):
    if next != 'http://0.0.0.0:5001/ui':
        flash('Bad redirect following login')
        return False
    return True

@app.route('/login', methods=['GET', 'POST'])
def login():
    global token
    token = None
    form = LoginForm()
    if form.validate_on_submit():
        # load user, and unicode formatted id count, login
        log = dbpass.userdb.find({ 'username': form.username.data })
        for thing in log:
            logi = thing
        id = u'{}'.format(logi['_id'])
        user = load_user(id)
        login_user(user, remember=form.remember_me.data)
        flash('Logged in, Good Job')
        if not is_safe_url('http://0.0.0.0:5001/ui'):
            return flask.abort(400)
        return flask.redirect('http://0.0.0.0:5001/ui')
    return render_template('login.html', title='Sign in', form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    global x
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, u'{}'.format(x))
        entry = { '_id': x, 'username': form.username.data, 'password': hash_password(form.password.data) }
        dbpass.userdb.insert_one(entry)
        return flask.redirect('http://0.0.0.0:5001/users/{}'.format('{}'.format(x)))
    return render_template('registration.html', form=form)

class Registration(Resource):
    def get(self, z):
        users = dbpass.userdb.find({'_id': z},{ 'password': 0 })
        for thing in users:
            user = thing
        user['password'] = 'hidden'
        return user

api.add_resource(Registration, '/users/<int:z>')

@app.route('/token', methods=["Get"])
@login_required
def token():
    tokenval = generate_auth_token(Config.SECRET_KEY)
    global token
    token = tokenval
    tokenvalue = { }
    tokenvalue['token'] = str(tokenval[1:])
    tokenvalue['expiration'] = 600
    return flask.jsonify(tokenvalue)


@app.route("/reauth", methods=["GET", "POST"])
@login_required
def reauth():
    if request.method == "POST":
        confirm_login()
        flash(u"Reauthenticated.")
        return redirect(request.args.get("next") or url_for("index"))
    return render_template("reauth.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(flask.url_for('ui'))
# -------------------------------
# Project 6 Below
# -------------------------------

@app.route('/')
def buttons():
    return render_template('buttons.html')


class All(Resource):
    @login_required
    def get(self, context='json'):
        global token
        if (token == None) or not (verify_auth_token(Config.SECRET_KEY, token)):
            flask.abort(401)
        getTop = reqparse.RequestParser()
        getTop.add_argument('top', type=int)
        stuff = getTop.parse_args()
        k = stuff['top']

        times = db.timedb.find()
        show = [time for time in times]
        
        if(context == 'csv'):
            show = '_id, OPEN, CLOSE\n'
            if(k):
                times = db.timedb.find(limit=k)
                for time in times:
                    dat = '{}, {}, {}\n'.format(time["_id"], time["OPEN"], time["CLOSE"])
                    show =+ dat
            else:
                times = db.timedb.find()
                for time in times:
                    dat = '{}, {}, {}\n'.format(time["_id"], time["OPEN"], time["CLOSE"])
                    show =+ dat
            result = show
        elif (context == 'json'):
            if(k):
                times = db.timedb.find(limit=k)
                show = [time for time in times]
                result = show 
            else:
                times = db.timedb.find()
                show = [time for time in times]
                result = show
        return result

class Open(Resource):
    @login_required
    def get(self, context='json'):
        global token
        if (token == None) or not (verify_auth_token(Config.SECRET_KEY, token)):
            abort(401)
        getTop = reqparse.RequestParser()
        getTop.add_argument('top', type=int)
        stuff = getTop.parse_args()
        k = stuff['top']
        if(context == 'csv'):
            show = '_id, OPEN'
            if(k):
                times = db.timedb.find({}, {"CLOSE": 0}, limit=k)
                for time in times:
                    dat = '{}, {}\n'.format(time["_id"], time["OPEN"])
                    show =+ dat
            else:
                times = db.timedb.find({}, {"CLOSE": 0})
                for time in times:
                    dat = '{}, {}\n'.format(time["_id"], time["OPEN"])
                    show =+ dat
            result = show
        elif (context == 'json'):
            if(k):
                times = db.timedb.find({}, {"CLOSE": 0}, limit=k)
                show = [time for time in times]
            else:
                times = db.timedb.find({}, {"CLOSE": 0})
                show = [time for time in times]
            result = show
        return result


class Close(Resource):
    @login_required
    def get(self, context='json'):
        global token
        if (token == None) or not (verify_auth_token(Config.SECRET_KEY, token)):
            flask.abort(401)
        getTop = reqparse.RequestParser()
        getTop.add_argument('top', type=int)
        stuff = getTop.parse_args()
        k = stuff['top']
        if(context == 'csv'):
            show = '_id, CLOSE\n'
            if(k):
                times = db.timedb.find({}, {"OPEN":0}, limit=k)
                for time in times:
                    dat = '{}, {}\n'.format(time['_id'], time['CLOSE'])
                    show =+ dat
            else:
                times = db.timedb.find({}, {"OPEN":0})
                for time in times:
                    dat = '{}, {}\n'.format(time['_id'], time['CLOSE'])
                    show =+ dat
            result = show
        elif (context == 'json'):
            if(k):
                times = db.timedb.find({}, {"OPEN": 0}, limit=k)
                show = [time for time in times]
            else:
                times = db.timedb.find({}, {"OPEN": 0})
                show = [time for time in times]
            result = show
        return result

api.add_resource(All, '/listAll', '/listAll/<string:context>')
api.add_resource(Open, '/listOpenOnly', '/listOpenOnly/<string:context>')
api.add_resource(Close, '/listCloseOnly', '/listCloseOnly/<string:context>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
