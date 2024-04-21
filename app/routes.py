from flask import render_template, url_for
from app import app
from forms import LoginForm

##Usage
# URLs need to be mapped to a function that will decide what happens on that page
# define the url using the @app.route decorator i.e '/test' = http://127.0.0.1:5000/test
# next a function is defined beneath the route that decides what happens at that URL

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
    return render_template('registration.html')

