import datetime
from app.db_helpers import db
from app.models import Posts

def test_new_post(new_post):
    '''
    GIVEN a Posts model
    WHEN a new post is created
    THEN check all fields are correctly defined
    '''
    assert new_post.name == "test_post"
    assert new_post.pay == 50
    assert new_post.start_from_date == datetime.date.today()
    assert new_post.status is "Open"
    
def test_query_posts(app_unit, new_post, new_user):
    '''
    GIVEN an app and a User and Posts model
    WHEN a new post is created and committed to the db
    THEN query the db and check that the results align with the new post
    '''
    with app_unit.app_context():
        db.session.add(new_post)
        db.session.commit
        
        assert Posts.query.first().author == new_user
        assert Posts.query.first().status == "Open"
        assert Posts.query.filter(Posts.status != 'Filled').first() != None
    