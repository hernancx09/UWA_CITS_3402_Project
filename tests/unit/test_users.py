from app.db_helpers import db
from app.models import Users

def test_new_user(new_user, app_unit):
    '''
    GIVEN a User model
    WHEN a new user is added to db
    THEN check username, display name and password fields are correctly stored
    '''
    with app_unit.app_context():
        db.session.add(new_user)
        db.session.commit
        
        assert Users.query.first().username == new_user.username
        assert Users.query.first().display_name == new_user.display_name
        assert Users.query.first().username == new_user.username