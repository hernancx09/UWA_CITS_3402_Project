from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, PasswordField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username is required.'),
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.')
    ])
    submit = SubmitField('Log in')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(message='Username is required.'),
        Length(min=4, max=25, message='Username must be between 4 and 25 characters long.'),
        Regexp('^[A-Za-z0-9_]+$', message='Username must contain only letters, numbers, and underscores.')
    ])
    display_name = StringField('Display-name', validators=[
        DataRequired(message='Display-name is required.'),
        Length(min=4, max=25, message='Display-name must be between 4 and 25 characters long.'),
        Regexp('^[a-zA-Z]+$', message='Display-name must contain only letters')
    ])
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

    
class PostForm(FlaskForm):
    job_name = StringField('Job Name')
    pay = IntegerField('Pay Rate p/hr')
    location = StringField('Location')
    job_type = SelectField(u'Job Type', choices=[('One Time'), ('Short Term'), ('Long Term')])
    start_from_date = DateField('Start Date')
    status = SelectField(u'Status', choices=[('Open'), ('Partially Filled'), ('Filled')])
    description = TextAreaField('Description')
    submit   = SubmitField('Post Job')
