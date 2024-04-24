import datetime
import pytest
from app import create_app
from app.models import Posts, Users
from config import Testing

@pytest.fixture(scope="session")
def app():
    app = create_app(config_class=Testing)
    
    yield app

@pytest.fixture(scope="session")
def client(app):
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture(scope="session")
def new_user():
    user = Users(username="test_user")
    user.set_display_name("test_user")
    user.set_password("test_password")
    return user

@pytest.fixture(scope="session")
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

