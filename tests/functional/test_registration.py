from app.models import Users
from app.db_helpers import *

def test_registration(client, app):
    response = client.post('/registration', data={
        "username": "new_user",
        "password": "password",
        "passwordCheck": "password",
    })
    assert b"new_user" in response.data
   
    with app.app_context():
        assert Users.query.count() == 1