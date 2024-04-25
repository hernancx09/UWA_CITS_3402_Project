from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
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
