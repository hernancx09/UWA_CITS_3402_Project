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
def client(app_functional):
    return app_functional.test_client()

@pytest.fixture(scope='module')
def new_user():
    user = Users(username="test_user")
    user.set_display_name("test_user")
    user.set_password("Test_password!")
    return user

@pytest.fixture(scope='module')
def new_post(new_user):
    post = Posts(
            author = new_user,
            user_id = new_user.get_id(),
            name = "test_post",
            pay = 50,
            location = "Perth",
            start_from_date = datetime.date.today(),
            description = "This is a new Job",
            job_type = "One Time",
            status = "Open"
        )
    return post

