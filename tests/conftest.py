import datetime
import pytest
from app import create_app
from app.models import Posts, Users
from config import Testing

@pytest.fixture(scope='session')
def app_functional():
    app = create_app(config_class=Testing)
    app.config['WTF_CSRF_ENABLED'] = False
    
    yield app

@pytest.fixture(scope='session')
def app_unit():
    app = create_app(config_class=Testing)
    app.config['WTF_CSRF_ENABLED'] = False
    
    yield app


@pytest.fixture(scope="function")
def client(app_functional, new_user):
    return app_functional.test_client()

@pytest.fixture(scope='module')
def new_user():
    user = Users(name="New User")
    user.set_email("newUser@gmail.com")
    user.set_password("Test_password!")
    return user

@pytest.fixture(scope='module')
def new_jobPost(new_user):
    post = Posts(
            author = new_user,
            user_id = new_user.get_id(),
            post_type = 0,
            name = "test_job",
            pay = 50,
            location = "Perth",
            start_from_date = datetime.date.today(),
            description = "This is a new Job",
            job_type = "One Time",
            status = "Open"
        )
    return post

@pytest.fixture(scope='module')
def new_skillsPost(new_user):
    post = Posts(
            author = new_user,
            user_id = new_user.get_id(),
            post_type = 1,
            name = "test_skills",
            location = "Perth",
            description = "These are my skills",
            job_type = "One Time",
        )
    return post
