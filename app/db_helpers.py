import datetime
import random
from flask_login import current_user
from app import db
from app.forms import PostJobForm, RegisterForm
from app.models import Messages, Users, Posts
import sqlalchemy as sa

POST_JOB = "Job request"

#get username from login form
def get_email(form):
        user = db.session.scalar(
                sa.select(Users).where(Users.email == form.email.data))
        return user

#add user to db
def create_user(form):
        user_email = get_email(form)
        if user_email is None:
                user = Users(name = form.name.data)
                user.set_email(form.email.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                return True
        return False

#create job post
def create_job(form):
        if(form.post_type.data == POST_JOB):
                post = Posts(
                        user_id = current_user.get_id(),
                        post_type = 0,
                        name = form.job_name.data,
                        pay = form.pay.data,
                        location = form.location.data,
                        job_type = form.job_type.data,
                        start_from_date = form.start_from_date.data,
                        status = form.status.data,
                        description = form.description.data
                )
        else:
                post = Posts(
                        user_id = current_user.get_id(),
                        post_type = 1,
                        name = form.looking_for.data,
                        location = form.location.data,
                        job_type = form.job_type.data,
                        description = form.description.data
                        )
        db.session.add(post)
        db.session.commit()
# edit job post
# Fetches user Posts and returns name, start_date, status and job type
def fetch_user_posts():
        data = db.session.query(Posts.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.status,
                                Posts.job_type,
                                Posts.id).filter(Posts.user_id == current_user.get_id())
        return data

def fetch_post_object(id):
        post = db.session.query(Posts).filter(Posts.id == id).first()
        return post
def fetch_post(id):
        data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.status,
                                Posts.job_type,
                                Posts.description).filter(Posts.id == id) \
                                        .filter(Posts.user_id == Users.id).first()
        return data
def fetch_all_jobPosts(keyword, job_type):
        if(job_type == "Any"):
                #Query on keyword alone
                data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.status,
                                Posts.job_type,
                                Posts.id,
                                Users.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Users.id == Posts.user_id) \
                                                .filter(Posts.post_type == 0) \
                                                        .filter(Posts.name.op('regexp')('^.*{}.*$'.format(keyword)), 
                                                     Posts.status != 'Filled').all()
        else:
                #query on keyword and job_type
                data = db.session.query(Posts.name,
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.status,
                                Posts.job_type,
                                Posts.id,
                                Users.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Users.id == Posts.user_id) \
                                                .filter(Posts.post_type == 0) \
                                                        .filter(Posts.name.op('regexp')('^.*{}.*$'.format(keyword)),
                                                     Posts.job_type == job_type, 
                                                     Posts.status != 'Filled').all()
        return data
def fetch_all_skillsPosts(keyword, job_type):
        if(job_type == "Any"):
                #Query on keyword alone
                data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.location,
                                Posts.job_type,
                                Posts.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Posts.user_id == Users.id) \
                                        .filter(Posts.post_type == 1) \
                                                .filter(Posts.name.op('regexp')('^.*{}.*$'.format(keyword))).all()
        else:
                #query on keyword and job_type
                data = db.session.query(Posts.name,
                                Users.name, 
                                Posts.location,
                                Posts.job_type,
                                Posts.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Posts.post_type == 1) \
                                                .filter(Posts.user_id == Users.id) \
                                                .filter(Posts.name.op('regexp')('^.*{}.*$'.format(keyword)),
                                             Posts.job_type == job_type).all()
        print(data)
        return data

def apply_for_job(form):
        msg = Messages(
                applicant_id = current_user.get_id(),
                job_id = form.job_id.data,
                employer_id = form.employer_id.data,
                message = form.message.data
        )
        db.session.add(msg)
        db.session.commit()

def fetch_received_messages():
        data = db.session.query(Posts.name,
                                Users.name, 
                                Users.email,
                                Messages.id).filter(current_user.get_id() == Messages.employer_id) \
                                        .filter(Messages.applicant_id == Users.id) \
                                                .filter(Posts.id == Messages.job_id).all()
        return data

def fetch_sent_messages():
        data = db.session.query(Posts.name,
                                Users.name,
                                Posts.status,
                                Posts.id).filter(current_user.get_id() == Messages.applicant_id) \
                                        .filter(Messages.employer_id == Users.id) \
                                                .filter(Posts.id == Messages.job_id).all()
        return data

def fetch_message(id):
        data = db.session.query(Users.name,
                                Users.email,
                                Messages.message).filter(Messages.employer_id== current_user.get_id()) \
                                        .filter(Users.id == Messages.applicant_id) \
                                                .filter(Messages.id == id).first()
        return data

'''DB populate helpers for testing'''
def get_random_user(int):
        user_id = db.session.query(Users.id).filter(Users.id == int).first().id
        return user_id

def populate_db(job_count, user_count):
    locations = [
        'Bassendean',
        'Joondalup',
        'Wembley',
        'Nedlands',
        'Cockburn',
        'Malaga',
        'Stirling',
        'Mt Lawley',
        'Mt Hawthorn',
        'Subiaco',
        'Maylands',
        'Bedford',
        'Dianella',
        'Inglewood',
        'Scarborough'
    ]
    job_type = [
        'One Time',
        'Short Term',
        'Long Term'
    ]
    user_names = [
            'Admin',
            'Chad',
            'Jack',
            'Tim',
            'Kelly',
            'Rachel',
            'Abi',
            'Louise',
            'Steve',
            'Hannah',
            'Daniel',
            'John',
            'Leon',
            'Carmel',
            'Ryan',
            'Matthew',
            'Justine',
            'Carol',
            'Shane',
            'Jasmine'
    ]
    date_start = datetime.date.today()
    date_end = datetime.date(2025, 12, 31)
    
    date_set = [datetime.date.today]
    
    while date_start != date_end:
        date_start += datetime.timedelta(days=1)
        date_set.append(date_start)
    j = 0
    while(j < user_count):     
        name = user_names[j]
        userForm = RegisterForm(
                name = "{}".format(name),
                email = "{}@gmail.com".format(name.lower()),
                password = "{}_user1".format(name),
                passwordCheck = "{}_user1".format(name),
        )
        create_user(userForm)
        j+=1
    if(job_count is not None):
        i = 0
        while (i < job_count):
            postForm = PostJobForm(
                    post_type = "Job request",
                    job_name = "Post {}".format(str(i)),
                    pay = random.randint(20, 100),
                    location = "{}".format(random.choice(locations)),
                    start_from_date = random.choice(date_set),
                    description = "This is a new Job",
                    job_type = random.choice(job_type),
                    status = "Open"
            )
            id = get_random_user(random.randint(1, user_count))
            post = Posts(
                            user_id = id,
                            post_type = 0,
                            name = postForm.job_name.data,
                            pay = postForm.pay.data,
                            location = postForm.location.data,
                            job_type = postForm.job_type.data,
                            start_from_date = postForm.start_from_date.data,
                            status = postForm.status.data,
                            description = postForm.description.data
                    )
            db.session.add(post)
            db.session.commit()
            i+=1
        
        
   
