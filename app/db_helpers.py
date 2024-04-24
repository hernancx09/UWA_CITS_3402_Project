from flask_login import current_user
from app import db
from app.models import Users, Posts
import sqlalchemy as sa

#get username from login form
def get_username(form):
        username = db.session.scalar(
                sa.select(Users).where(Users.username == form.username.data))
        return username

#add user to db
def create_user(form):
        user = get_username(form)
        print(user)
        if user is None:
                user = Users(username = form.username.data)
                user.set_display_name(form.display_name.data)
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
def fetch_all_posts():
        data = db.session.query(Posts.name, Posts.pay, sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'), Posts.location, Posts.job_type).filter(Posts.status != 'Filled')
        return data()