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
        
        assert Users.query.first().name == new_user.name
        assert Users.query.first().email == new_user.email
        assert Users.query.first().password_hash != "Test_password!"