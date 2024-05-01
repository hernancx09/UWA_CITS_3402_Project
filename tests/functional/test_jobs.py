from flask_login import login_user
from app.db_helpers import db

def test_main_search(client, app_functional, new_jobPost, new_user):
    """
    GIVEN a test client, app
    WHEN new post is created in db and the '/jobs' page sends a post request with search data
    THEN check that the response is 200 and results are correct
    """
    with app_functional.app_context():
        '''
        1. with app context push new post to db
        2. make post request to main with search data
        3. check that db is queried and returns correct result
        '''
        with app_functional.test_request_context():
            login_user(new_user)
        
        db.session.add(new_jobPost)
        db.session.commit
        
        response = client.post('/jobs', data= dict(
            keyword = "test",
            job_type = "Any",
            follow_redirects=True))

        assert response.status_code == 200
        assert new_jobPost.name.encode('ASCII') in response.data
        assert new_user.name.encode('ASCII') in response.data
        assert str(new_jobPost.pay).encode('ASCII') in response.data
        assert new_jobPost.location.encode('ASCII') in response.data
        assert new_jobPost.start_from_date.strftime("%d/%m/%Y").encode('ASCII') in response.data
        assert new_jobPost.status.encode('ASCII') in response.data
        assert new_jobPost.job_type.encode('ASCII') in response.data