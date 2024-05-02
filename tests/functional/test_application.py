from flask_login import login_user, logout_user
from app.db_helpers import db
from app.models import Messages, Posts, Users


def test_main_search(client, app_functional, new_jobPost, new_user):
    """
    GIVEN a test client, app
    WHEN user applies for a job
    THEN check that the employer is inboxed with user details, also check applicants profile shows application
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

        print("\n username:" + str(Users.query.all()[0].name) + ", id:" + str(Users.query.all()[0].id))
        print("\n username:" + str(Users.query.all()[1].name) + ", id:" + str(Users.query.all()[1].id))
        print("\n username:" + str(Users.query.all()[2].name) + ", id:" + str(Users.query.all()[2].id))
        
        msg = Messages(
            message = "new application",
            job_id = 1,
            employer_id = 3,
            applicant_id = 2
        )
    
        db.session.add(msg)
        db.session.commit
        with app_functional.test_request_context():
            login_user(new_user)
            
        response = client.get('/profile')
        
        assert response.status_code == 200
        assert b"Messages" in response.data
        assert b"My Applications" in response.data
        assert b"My Ongoing Jobs" in response.data
        assert user.name.encode('ASCII') in response.data
        assert user.email.encode('ASCII') in response.data

        '''
        1. switch to user 2
        2. check user 2 profile shows they have applied
        '''
        with app_functional.test_request_context():
            logout_user()
            login_user(user)
        
        response = client.get('/profile')
        job_name = Posts.query.filter(Posts.id == 1).first().name
        
        assert response.status_code == 200
        assert b"Messages" in response.data
        assert b"My Applications" in response.data
        assert b"My Ongoing Jobs" in response.data
        assert new_user.name.encode('ASCII') in response.data
        assert job_name.encode('ASCII') in response.data