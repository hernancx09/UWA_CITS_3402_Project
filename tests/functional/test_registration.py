
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
    

    