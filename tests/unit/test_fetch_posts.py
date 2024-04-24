import datetime
from platform import node
import sqlalchemy as sa
from app.db_helpers import *
from app.models import Posts

def test_post_exists(new_post):
    assert new_post.name == "test_post"
    assert new_post.pay == 50
    assert new_post.start_from_date == datetime.date.today()
    assert new_post.status is not "Filled"
    
def test_query_posts(app, new_post, new_user):
    with app.app_context():
        db.session.add(new_post)
        db.session.commit
        
        assert Posts.query.first().author == new_user
        assert Posts.query.first().status != "Filled"
        assert Posts.query.filter(Posts.status != 'Filled').first() != None
    