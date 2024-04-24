import pytest
from app import create_app
from app.models import Users
from config import Testing

@pytest.fixture(scope="session")
def client():
    app = create_app(config_class=Testing)
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

@pytest.fixture(scope="module")
def new_user():
    user = Users(username="test_user")
    user.set_password("test_password")
    return user

