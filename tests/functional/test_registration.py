from app.db_helpers import *
from app.forms import RegisterForm

def test_registration(client):
    response = client.post('/registration', data={
        "username": "new_user",
        "password": "password",
        "passwordCheck": "password",
    })
    
    assert response.status_code == 200
    assert b"new_user" in response.data
    assert b"password" in response.data

    