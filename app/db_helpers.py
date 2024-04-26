from flask_login import current_user
from app import db
from app.models import Users, Posts
import sqlalchemy as sa

#get username from login form
def get_email(form):
        email = db.session.scalar(
                sa.select(Users).where(Users.email == form.email.data))
        return email

#add user to db
def create_user(form):
        user_email = get_email(form)
        print(user_email)
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
        post = Posts(
                name = form.job_name.data,
                pay = form.pay.data,
                location = form.location.data,
                job_type = form.job_type.data,
                start_from_date = form.start_from_date.data,
                status = form.status.data,
                description = form.description.data
        )
        db.session.add(post)
        db.session.commit()
#edit job post
# Fetches user posts and returns name, start_date, status and job type
def fetch_user_posts():
        data = db.session.query(Posts.name, sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'), Posts.job_type, Posts.status).filter(Posts.user_id == current_user.get_id())
        return data
def fetch_all_posts(keyword, job_type):
        if(job_type == "Any"):
                #Query on keyword alone
                data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.status,
                                Posts.job_type).filter(Users.id == Posts.user_id).filter(Posts.name.op('regexp')('^.*{}.*$'.format(keyword)), 
                                                     Posts.status != 'Filled').all()
        else:
                #query on keyword and job_type
                data = db.session.query(Posts.name,
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.status,
                                Posts.job_type).filter(Users.id == Posts.user_id).filter(Posts.name.op('regexp')('^.*{}.*$'.format(keyword)),
                                                     Posts.job_type == job_type, 
                                                     Posts.status != 'Filled').all()
        return data