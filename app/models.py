from datetime import date
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index = True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    posts: so.WriteOnlyMapped['Posts'] = so.relationship(back_populates='user_id')
    def __repr__(self):
        return '<User {}>'.format(self.username)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Posts(db.Model):
    author: so.Mapped[Users] = so.relationship(back_populates='posts')
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key= True)
    name: so.Mapped[str] = so.mapped_column(sa.String(32), index = True)
    pay: so.Mapped[str] = so.mapped_column(sa.String(16))
    location: so.Mapped[str] = so.mapped_column(sa.String(16))
    job_type: so.Mapped[str] = so.mapped_column(sa.String(16))
    start_from_date: so.Mapped[date] = so.mapped_column(sa.Date())
    status: so.Mapped[str] = so.mapped_column(sa.String(32))
    description: so.Mapped[str] = so.mapped_column(sa.String(256))