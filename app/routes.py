
from flask import flash, render_template, request, redirect, url_for, flash

from flask import current_app
from app.db_helpers import create_job, create_user, fetch_all_jobPosts, fetch_all_skillsPosts, get_email, populate_db
from app.forms import DataForm, LoginForm, PostJobForm, RegisterForm, SearchForm
from flask_login import current_user, login_required, login_user, logout_user

##Usage
# URLs need to be mapped to a function that will decide what happens on that page
# define the url using the @app.route decorator i.e '/test' = http://127.0.0.1:5000/test
# next a function is defined beneath the route that decides what happens at that URL

'''
@current_app.route('/base')
def base():
    return render_template('base.html')
'''
@current_app.route('/')
@current_app.route('/about')
def about():
    return render_template('about.html')

'''
TESTING PURPOSES ONLY
'''
@current_app.route('/populate', methods=['GET', 'POST'])
def populate():
    form = DataForm()
    if(form.validate_on_submit()):
        populate_db(form.job_count.data, form.user_count.data)
        return redirect(url_for('login'))
    return render_template('populate.html', form = form)
''' END TESTS'''

@current_app.route('/jobs', methods=['GET', 'POST'])
@login_required
def jobs():
    searchForm = SearchForm()
    
    if(searchForm.validate_on_submit()):
        result = fetch_all_jobPosts(searchForm.keyword.data, searchForm.job_type.data)  
        if (result == []): # if result empty
            result = [('-', '-', '-', '-', '-', '-', '-')]
        return render_template('jobs.html', form = searchForm, data = result)
    
    result = fetch_all_jobPosts("", "Any")
    return render_template('jobs.html', form = searchForm, data = result)

@current_app.route('/candidates', methods=['GET', 'POST'])
@login_required
def candidates():
    searchForm = SearchForm()
    
    if(searchForm.validate_on_submit()):
        result = fetch_all_skillsPosts(searchForm.keyword.data, searchForm.job_type.data)  
        if (result == []): # if result empty
            result = [('-', '-', '-', '-', '-', '-', '-')]
        return render_template('candidates.html', form = searchForm, data = result)
    
    result = fetch_all_skillsPosts("", "Any")
    return render_template('candidates.html', form = searchForm, data = result)

@current_app.route('/login', methods=['GET', 'POST'])
def login():
    if(current_user.is_authenticated):
        flash("You are already logged in!")
        return redirect(url_for('jobs'))
    form = LoginForm()

    if(form.validate_on_submit()):
        user = get_email(form)
        if user is None or not user.check_password(form.password.data):
            flash("Invalid email or password", "message")
            return redirect(url_for('login'))
        flash("Welcome {}".format(user.name))
        login_user(user)
        return redirect(url_for('jobs'))
    
    return render_template('login.html', form=form)

@current_app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('about'))

@current_app.route('/registration', methods = ['GET','POST'])
def registration():
    regform = RegisterForm()

    if(regform.validate_on_submit()):
        if(create_user(regform)):
            #success, sending to test.html as a placeholder
            flash('Success Registering', 'Success')
            return redirect(url_for('login')) # should return to login page to login
        else:
            #return the registration form with error message perhaps?
            flash('Error Registering', 'Failure')
            return redirect(url_for('registration'))  

    return render_template('registration.html', form = regform)

@current_app.route('/post', methods = ['GET','POST'])
@login_required
def post():
    postForm = PostJobForm()
    
    if(postForm.validate_on_submit()):
        create_job(postForm)
        return render_template('post.html', form = PostJobForm())
    return render_template('post.html', form = postForm)

@current_app.route('/profile')
def profile():
    return render_template('profile.html')


#Main Job
@current_app.route('/jd')
def jd():
    return render_template('job-detail.html')




@current_app.route('/view')
def view():
    return render_template('view.html')



@current_app.route('/detail')
def detail():
    return render_template('details.html')