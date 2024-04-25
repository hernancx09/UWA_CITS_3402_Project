from app.db_helpers import db
import sqlalchemy as sa

def test_main_search(client, app_functional, new_post, new_user):
    """
    GIVEN a test client, app
    WHEN new post is created in db and the '/main' page sends a post request with search data
    THEN check that the response is 200 and results are correct
    """
    with app_functional.app_context():
        '''
        1. with app context push new post to db
        2. make post request to main with search data
        3. check that db is queried and returns correct result
        '''
        db.session.add(new_post)
        db.session.commit
        
        response = client.post('/main', data= dict(
            keyword = "test",
            job_type = "Any",
            follow_redirects=True))

        assert response.status_code == 200
        assert new_post.name.encode('ASCII') in response.data
        assert new_user.name.encode('ASCII') in response.data
        assert str(new_post.pay).encode('ASCII') in response.data
        assert new_post.location.encode('ASCII') in response.data
        assert new_post.start_from_date.strftime("%d/%m/%Y").encode('ASCII') in response.data
        assert new_post.status.encode('ASCII') in response.data
        assert new_post.job_type.encode('ASCII') in response.data