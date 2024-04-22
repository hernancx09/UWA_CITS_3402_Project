from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit   = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    passwordCheck = PasswordField('Password')
    submit   = SubmitField('Register')