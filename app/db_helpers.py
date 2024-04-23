from app import db
from app.models import Users
import sqlalchemy as sa

#get username from login form
def get_username(form):
        username = db.session.scalar(
                sa.select(Users).where(Users.username == form.username.data))
        return username
#add user to db
def create_user(form):
        user = get_username(form)
        if user is None:
                user = Users(username = form.username.data)
                user.set_password(form.password.data)
                db.session.add(user)
                db.session.commit()
                return True
        return False