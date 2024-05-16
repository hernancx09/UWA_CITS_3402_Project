import datetime
import random
from flask_login import current_user
from app import db
from app.forms import PostJobForm, RegisterForm
from app.models import Messages, Users, Posts
import sqlalchemy as sa

#CONSTANTS
REQUEST = "Job request"
LOOKING = "Looking for work"

#Checks if formdata containes unique email, if so returns user object tied to the email
def check_unique_email(form):
        user = db.session.scalar(
                sa.select(Users).where(Users.email == form.email.data))
        return user

#add user to db from formdata
def create_user(form):
        user_email = check_unique_email(form)
        if user_email is None:
                user = Users(name = form.name.data)
                user.set_email(form.email.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                return True
        return False

#create job post from formdata
def create_post(form):
        post = Posts(
                user_id = current_user.get_id(),
                post_type = form.post_type.data,
                name = form.name.data,
                pay = form.pay.data,
                location = form.location.data,
                job_type = form.job_type.data,
                start_from_date = form.start_from_date.data,
                description = form.description.data
        )
        db.session.add(post)
        db.session.commit()
        
#remove post from db given post id
def delete_post(job_id):
        post = fetch_post_object(job_id)
        db.session.delete(post)
        db.session.commit()
        
#pre fill post form with job details given post id
def pre_fill_post_form(job_id):
        post = fetch_post_object(job_id)
        form = PostJobForm(
            post_type = post.post_type,
            name = post.name,
            pay= str(post.pay),
            location = post.location,
            job_type = post.job_type,
            start_from_date = post.start_from_date,
            description = post.description
        )
        return form

# edit job post from formdata 
def update_job(form, post_id):
        post = Posts.query.filter(Posts.id == post_id).first()
        form.populate_obj(post)

        db.session.add(post)
        db.session.commit()
        
# Fetches ALL user Posts data
def fetch_user_posts():
        data = db.session.query(Posts.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.job_type,
                                Posts.id).filter(Posts.user_id == current_user.get_id())
        return data

# Fetch specific post object
def fetch_post_object(id):
        post = db.session.query(Posts).filter(Posts.id == id).first()
        return post

# Fetch specific post data from db 
def fetch_post(id):
        data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.job_type,
                                Posts.description,
                                Posts.id,
                                Posts.user_id).filter(Posts.id == id) \
                                        .filter(Posts.user_id == Users.id).first()
        return data

# Fetch ALL job posts from db not made by user
def fetch_all_jobPosts(keyword, job_type):
        if(job_type == "Any"):
                #Query on keyword alone 
                data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.job_type,
                                Posts.id,
                                Users.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Users.id == Posts.user_id) \
                                                .filter(Posts.post_type == REQUEST) \
                                                        .filter(sa.func.lower(Posts.name).op('regexp')('^.*{}.*$'.format(keyword))).all()
        else:
                #query on keyword and job_type
                data = db.session.query(Posts.name,
                                Users.name, 
                                Posts.pay,
                                Posts.location,
                                sa.text('STRFTIME("%d/%m/%Y",Posts.start_from_date)'),
                                Posts.job_type,
                                Posts.id,
                                Users.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Users.id == Posts.user_id) \
                                                .filter(Posts.post_type == REQUEST) \
                                                        .filter(sa.func.lower(Posts.name).op('regexp')('^.*{}.*$'.format(keyword)),
                                                     Posts.job_type == job_type).all()
        return data

# Fetch ALL skill posts from db not made by user
def fetch_all_skillsPosts(keyword, job_type):
        if(job_type == "Any"):
                #Query on keyword alone
                data = db.session.query(Posts.name, 
                                Users.name, 
                                Posts.location,
                                Posts.job_type,
                                Posts.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Posts.user_id == Users.id) \
                                        .filter(Posts.post_type == LOOKING) \
                                                .filter(sa.func.lower(Posts.name).op('regexp')('^.*{}.*$'.format(keyword))).all()
        else:
                #query on keyword and job_type
                data = db.session.query(Posts.name,
                                Users.name, 
                                Posts.location,
                                Posts.job_type,
                                Posts.id).filter(current_user.get_id() != Posts.user_id) \
                                        .filter(Posts.post_type == LOOKING) \
                                                .filter(Posts.user_id == Users.id) \
                                                .filter(sa.func.lower(Posts.name).op('regexp')('^.*{}.*$'.format(keyword)),
                                             Posts.job_type == job_type).all()
        return data

# Add message to db from formdata
def apply_for_job(form):
        msg = Messages(
                applicant_id = current_user.get_id(),
                job_id = form.job_id.data,
                employer_id = form.employer_id.data,
                message = form.message.data
        )
        db.session.add(msg)
        db.session.commit()

# Fetch user received messages
def fetch_received_messages():
        data = db.session.query(Posts.name,
                                Users.name, 
                                Users.email,
                                Messages.id).filter(current_user.get_id() == Messages.employer_id) \
                                        .filter(Messages.applicant_id == Users.id) \
                                                .filter(Posts.id == Messages.job_id).all()
        return data

# Fetch user sent messages
def fetch_sent_messages():
        data = db.session.query(Posts.name,
                                Users.name,
                                Messages.job_id).filter(current_user.get_id() == Messages.applicant_id) \
                                        .filter(Messages.employer_id == Users.id) \
                                                .filter(Posts.id == Messages.job_id).all()
        return data

# Fetch specific user received message
def fetch_message(id):
        data = db.session.query(Users.name,
                                Users.email,
                                Messages.message).filter(Messages.employer_id== current_user.get_id()) \
                                        .filter(Users.id == Messages.applicant_id) \
                                                .filter(Messages.id == id).first()
        return data

# DB POPULATOR HELPER FUNCTIONS --- TESTING ONLY
def get_random_user(int):
        user_id = db.session.query(Users.id).filter(Users.id == int).first().id
        return user_id

def populate_db(job_count, user_count):
        jobs = [
                'Mow my lawn',
                'Elderly Shopping Delivery',
                'Flower Delivery Driver',
                'Help me move house',
                'Change my car tyre',
                'Maths Tutor',
                'Teacher',
                'Lab Assistant',
                'Bricklayer',
                'Electrician',
                'Mechanic',
                'Painter',
                'Builder',
                'Junior Web Developer',
                'CAD Technician',
                'Full Stack Developer',
                'IT Technician',
                'Software Developer',
                'Network Administrator',
                'System Administrator'
        ]
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
        # Build set of dates from today to 6 months from now
        date_start = datetime.date.today()
        date_end = datetime.date(datetime.date.today().year, datetime.date.today().month + 6, 28)
        date_set = [datetime.date.today]
        
        while date_start != date_end:
            date_start += datetime.timedelta(days=1)
            date_set.append(date_start)
        #---------------------------------------------------
        # Create random users
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
        #---------------------------------------------------
        # Create random job posts
        if(job_count is not None):
            i = 0
            while (i < job_count):
                postForm = PostJobForm(
                        post_type = REQUEST,
                        name = random.choice(jobs),
                        pay = random.randint(20, 100),
                        location = "{}".format(random.choice(locations)),
                        start_from_date = random.choice(date_set),
                        description = "This is a job description...",
                        job_type = random.choice(job_type)
                )
                id = get_random_user(random.randint(1, user_count))
                post = Posts(
                                user_id = id,
                                post_type = REQUEST,
                                name = postForm.name.data,
                                pay = postForm.pay.data,
                                location = postForm.location.data,
                                job_type = postForm.job_type.data,
                                start_from_date = postForm.start_from_date.data,
                                description = postForm.description.data
                        )
                db.session.add(post)
                db.session.commit()
                i+=1
        #---------------------------------------------------
        # Create random Skill posts = half job count
            i=0
            while(i < job_count/2):
                    postForm = PostJobForm(
                        post_type = LOOKING,
                        name = "Post {}".format(str(i)),
                        location = "{}".format(random.choice(locations)),
                        description = "Looking for some work",
                        job_type = random.choice(job_type)
                    )
                    id = get_random_user(random.randint(1, user_count))
                    post = Posts(
                                    user_id = id,
                                    post_type = LOOKING,
                                    name = postForm.name.data,
                                    location = postForm.location.data,
                                    job_type = postForm.job_type.data,
                                    description = postForm.description.data
                            )
                    db.session.add(post)
                    db.session.commit()
                    i+=1
        #---------------------------------------------------
# ---------------------- END TESTING FUNCTIONS -------------------------  
