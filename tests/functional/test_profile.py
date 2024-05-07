import datetime
from flask_login import current_user, login_user
from app.models import Messages, Posts, Users
from app.db_helpers import db


def test_profile_page(client, app_functional, new_user):
    """
    GIVEN a test client
    WHEN the user logs in and navigates to profile page
    THEN check that the response is valid and data is valid for that user
    """
    client.post('/registration', data= dict(
        name = "Jimmy",
        email = "jimmy@gmail.com",
        password = "Password1",
        passwordCheck = "Password1"), follow_redirects=True)
    
    client.post('/registration', data= dict(
        name = "Abi",
        email = "abi@gmail.com",
        password = "Password1",
        passwordCheck = "Password1"), follow_redirects=True)
    
    with app_functional.app_context():
        post = Posts(
            author = Users.query.first(),
            user_id = Users.query.first().id,
            post_type = "Job request",
            name = "test_job",
            pay = 50,
            location = "Perth",
            start_from_date = datetime.date.today(),
            description = "This is a new Job",
            job_type = "One Time",
            status = "Open"
        )
        db.session.add(post)
        db.session.commit
        
        message = Messages(
            job_id = Posts.query.first().id,
            applicant_id = Users.query.filter(Users.name == "Abi").first().id,
            employer_id = Users.query.filter(Users.name == "Jimmy").first().id,
            message = "Hi Jimmy"
        )
        db.session.add(message)
        db.session.commit
            
        with app_functional.test_request_context():
            login_user(Users.query.first())

            response = client.get('/profile')
        
            assert response.status_code == 200
            assert response.request.path == "/profile"
            assert b"My Ongoing Jobs" in response.data
            assert b"My Applications" in response.data
            assert b"Messages" in response.data
            assert b"test_job" in response.data
            assert b"abi@gmail.com" in response.data
            
            client.post('/profile', data = dict(
                post_id = Posts.query.first().id))

            response = client.get('/profile')
            
            assert response.status_code == 200
            assert response.request.path == "/profile"
            assert b"My Ongoing Jobs" in response.data
            assert b"My Applications" in response.data
            assert b"Messages" in response.data
            assert b"test_job" not in response.data
            assert b"abi@gmail.com" not in response.data
