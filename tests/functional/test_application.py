from flask_login import login_user
from app.db_helpers import db
from app.models import Messages, Users


def test_main_search(client, app_functional, new_jobPost, new_user):
    """
    GIVEN a test client, app
    WHEN user applies for a job
    THEN check that the employer is inboxed with user details
    """
    with app_functional.app_context():
        '''
        1. create user 2, push user 1 post to db
        2. login as user 1 and user 2 apply for user 1 job
        3. check user 1 inbox contains user 2 details
        '''
        user = Users(name="Tim")
        user.set_email("tim@gmail.com")
        user.set_password("Test_password!")
        
        db.session.add(user)
        db.session.add(new_jobPost)
        db.session.commit

        with app_functional.test_request_context():
            login_user(new_user)
            
        msg = Messages(
            message = "new application",
            job_id = 1,
            employer_id = 3,
            applicant_id = 2
        )
    
        db.session.add(msg)
        db.session.commit
        
        response = client.get('/profile')
        assert response.status_code == 200
        assert b"Messages" in response.data
        assert b"My Applications" in response.data
        assert b"My Ongoing Jobs" in response.data
        assert user.name.encode('ASCII') in response.data
        assert user.email.encode('ASCII') in response.data
