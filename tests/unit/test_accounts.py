from app.models import Users
from app.db_helpers import *

def test_user_exists(app):
    with app.app_context():
        user = Users(username="test")
        db.session.add(user)
        db.session.commit()
        
        assert Users.query.count() == 1
        assert Users.query.first().username == "test"