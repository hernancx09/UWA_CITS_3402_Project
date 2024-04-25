
def test_main_invalid_request(client):
    """
    GIVEN a test client
    WHEN the '/main' page sends a post request
    THEN check that the response is 405
    """
    response = client.post('/main')

    assert response.status_code == 405