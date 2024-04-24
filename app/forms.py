from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, PasswordField, SubmitField, IntegerField, TextAreaField

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    submit   = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    passwordCheck = PasswordField('Password')
    submit   = SubmitField('Register')
    
class PostForm(FlaskForm):
    job_name = StringField('Job Name')
    pay = IntegerField('Pay Rate p/hr')
    location = StringField('Location')
    job_type = SelectField(u'Job Type', choices=[('One Time'), ('Short Term'), ('Long Term')])
    start_from_date = DateField('Start Date')
    status = SelectField(u'Status', choices=[('Open'), ('Partially Filled'), ('Filled')])
    description = TextAreaField('Description')
    submit   = SubmitField('Post Job')
