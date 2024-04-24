from flask import flash, render_template, request, redirect, url_for, flash
from flask import current_app
from app.db_helpers import create_user, get_username
from app.forms import LoginForm, PostForm, RegisterForm
from flask_login import current_user, login_required, login_user, logout_user

##Usage
# URLs need to be mapped to a function that will decide what happens on that page
# define the url using the @app.route decorator i.e '/test' = http://127.0.0.1:5000/test
# next a function is defined beneath the route that decides what happens at that URL
@current_app.route('/')
@current_app.route('/base')
def test():
    return render_template('base.html')

@current_app.route('/main')
def main():
    return render_template('main.html')

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    '''
    if form.validate_on_submit():
        run code below to check for error
    '''
    #user = get_username(form)
    #if user is None or not user.check_password(form.password.data):
    #    #some error message, not sure how we want to do that yet, flash is an easy way
    #    print('Error')
    #    return redirect(url_for('login'))
    '''
    else we just run the following using flask_login
        login_user(user)
        return some redirect
    '''
    return render_template('login.html', form=form)

@current_app.route('/registration', methods = ['GET','POST'])
def registration():
    Regform = RegisterForm()
    if(Regform.validate_on_submit()):
        if(create_user(Regform)):
            #success, sending to test.html as a placeholder
            flash('Success Registering', 'Success')
            return redirect(url_for('login')) # should return to login page to login
        else:
            #return the registration form with error message perhaps?
            flash('Error Registering', 'Failure')
            return redirect(url_for('registration'))  
    return render_template('registration.html', form = Regform)

@current_app.route('/post', methods = ['GET','POST'])
#@login_required
def post():
    form = PostForm()
    return render_template('post.html', form = form)