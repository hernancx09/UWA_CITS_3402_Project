
def test_registration_valid_data(client):
    """
    GIVEN a test client
    WHEN the '/registration' page is posted with valid data
    THEN check that the response is valid
    """
    response = client.post('/registration', data= dict(
        name = "Jimmy",
        email = "jimmy@gmail.com",
        password = "Password1",
        passwordCheck = "Password1"), follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == "/login"
    
def test_registration_invalid_data(client):
    """
    GIVEN a test client
    WHEN the '/registration' page is posted with invalid password data
    THEN check that the response is invalid
    """
    response = client.post('/registration', data= dict(
        name = "Jimmy",
        email = "jimmy@gmail",
        password = "Password1",
        passwordCheck = "Password"), follow_redirects=True)

    assert response.request.path == "/registration"

def test_login_valid_data(client, app_functional):
    """
    GIVEN a test client
    WHEN the '/login' page is posted with valid data
    THEN check that the response is valid
    """
    with app_functional.test_request_context():
        response = client.post('/login', data=dict(
            email = "jimmy@gmail.com",
            password = "Password1"
        ), follow_redirects=True)
        assert response.status_code == 200
        assert response.request.path == "/jobs"

def test_login_invalid_data(client, app_functional):
    """
    GIVEN a test client
    WHEN the '/login' page is posted with invalid data
    THEN check that the response is redirect to login and flashed message is in response
    """
    with app_functional.test_request_context():
        response = client.post('/login', data=dict(
            email = "jimmy@gmail.com",
            password = "password1"
        ), follow_redirects=True)
        
        assert b"Invalid email or password" in response.data
        assert response.status_code == 200
        assert response.request.path == "/login"