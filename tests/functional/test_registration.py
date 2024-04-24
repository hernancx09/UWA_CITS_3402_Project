from app.db_helpers import *
from app.forms import RegisterForm

def test_registration(client):
    response = client.post('/registration', data= dict(
        username = "newuser",
        display_name = "newdisplay",
        password = "Password1",
        passwordCheck = "Password1"), follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == "/login"
    
    

    