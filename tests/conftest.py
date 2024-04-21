import pytest
from app import create_app
from config import Testing

@pytest.fixture()
def app():
    app = create_app(config_class=Testing)
    
    yield app
    
@pytest.fixture()
def client(app):
    return app.test_client()