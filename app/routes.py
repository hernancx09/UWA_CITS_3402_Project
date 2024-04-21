from flask import render_template
from app import app
from app.forms import LoginForm, RegisterForm

##Usage
# URLs need to be mapped to a function that will decide what happens on that page
# define the url using the @app.route decorator i.e '/test' = http://127.0.0.1:5000/test
# next a function is defined beneath the route that decides what happens at that URL
app.config['SECRET_KEY'] = 'potatoe'
@app.route('/')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/registration')
def registration():
    Regform = RegisterForm()
    return render_template('registration.html', form = Regform)

