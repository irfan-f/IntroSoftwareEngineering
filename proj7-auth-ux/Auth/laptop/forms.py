from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, HiddenField
from wtforms.validators import DataRequired, ValidationError
import wtforms.validators
from password import verify_password
from pymongo import MongoClient
import os

client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.passdb

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    val = HiddenField('')
    submit = SubmitField('Sign in')
    def validate_username(FlaskForm, field):
        user = db.userdb.count({ 'username': field.data })
        if user == 0:
            raise ValidationError('Username is incorrect')
        else:
            FlaskForm.val.data = '1'
    def validate_password(FlaskForm, field):
        if FlaskForm.val.data == '1':
            for x in db.userdb.find({'username': FlaskForm.username.data}):
                hsval = x['password']
            if not verify_password(field.data, hsval):
               raise ValidationError('Password is incorrect.')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    def validate_username(FlaskForm, field):
        if db.userdb.count({ 'username': field.data}) == 1:
            raise ValidationError('User already exists')
