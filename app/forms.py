from flask_wtf import FlaskForm

from wtforms import DateField, SelectField, StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, Email, Optional

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),

    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.')
    ])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):

    name = StringField('Name', validators=[
        DataRequired(message='Name is required.'),
        Length(min=4, max=25, message='Name must be between 4 and 25 characters long.'),
        Regexp('^[A-Za-z ]+$', message='Name must contain only letters')
    ])
    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.'),
        Length(min=6, message='Password must be at least 6 characters long.'),
        Regexp('^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).+$', message='Password must include at least one lowercase letter, one uppercase letter, and one digit.')
    ])
    passwordCheck = PasswordField('Confirm Password', validators=[
        DataRequired(message='Password confirmation is required.'),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Register')

class SearchForm(FlaskForm):
    keyword = StringField('Keyword', validators=[Optional()])
    job_type = SelectField(u'Job Type', choices=[('Any'), ('One Time'), ('Short Term'), ('Long Term')])
    submit = SubmitField('Go')

class PostForm(FlaskForm):
    job_name = StringField('Job Name')
    pay = IntegerField('Pay Rate p/hr')
    location = StringField('Location')
    job_type = SelectField(u'Job Type', choices=[('One Time'), ('Short Term'), ('Long Term')])
    start_from_date = DateField('Start Date')
    status = SelectField(u'Status', choices=[('Open'), ('Partially Filled'), ('Filled')])
    description = TextAreaField('Description')
    submit   = SubmitField('Post Job')

