import datetime
from app.db_helpers import db
from app.models import Posts

def test_query_jobPosts(app_unit, new_jobPost, new_skillsPost, new_user):
    '''
    GIVEN an app and a User and Posts model
    WHEN a new post is created and committed to the db
    THEN query the db and check that the results align with the new post
    '''
    with app_unit.app_context():
        db.session.add(new_jobPost)
        db.session.commit
        
        assert Posts.query.first().author == new_user
        assert Posts.query.first().status == "Open"
        assert Posts.query.filter(Posts.status != 'Filled').first() != None
        
        db.session.delete(new_jobPost)
        db.session.commit
    
        db.session.add(new_skillsPost)
        db.session.commit
        
        assert Posts.query.first() is not None
        assert Posts.query.first().author == new_user
        assert Posts.query.first().status == None
        assert Posts.query.filter(Posts.post_type != 0).first() != None
        
        db.session.delete(new_skillsPost)
        db.session.commit

