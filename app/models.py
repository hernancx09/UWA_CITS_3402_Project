from datetime import date
from typing import Optional
from flask_login import UserMixin
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model, UserMixin):
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64))
    email: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    posts: so.WriteOnlyMapped['Posts'] = so.relationship(back_populates='author')
    def __repr__(self):
        return '<User {}>'.format(self.name)
    def set_email(self, email):
        self.email = email
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    def get_user_id(self):
        return self.id

@login.user_loader
def load_user(id):
    return db.session.get(Users, int(id))

# Posts table data will change depending on post type
# i.e. pay and start from date will be null
class Posts(db.Model):
    author: so.Mapped[Users] = so.relationship(back_populates='posts')
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Users.id), index=True)
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key= True)
    post_type: so.Mapped[str] = so.mapped_column(sa.String(16))
    name: so.Mapped[str] = so.mapped_column(sa.String(32), index = True)
    pay: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=True)
    location: so.Mapped[str] = so.mapped_column(sa.String(16))
    job_type: so.Mapped[str] = so.mapped_column(sa.String(16))
    start_from_date: so.Mapped[date] = so.mapped_column(sa.Date(), nullable=True)
    description: so.Mapped[str] = so.mapped_column(sa.String(256))
    
    def __repr__(self):
        return '<name {}, author {}>'.format(self.name, self.author)
    def set_pay(self, pay):
        self.pay = pay
    def set_type(self, type):
        self.job_type = type
    def set_description(self, description):
        self.description = description

class Messages(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer(), primary_key= True)
    job_id: so.Mapped[int] = so.mapped_column(sa.Integer())
    applicant_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Users.id), index=True)
    employer_id: so.Mapped[int] = so.mapped_column(sa.Integer())
    message: so.Mapped[str] = so.mapped_column(sa.String(256))
    def __repr__(self):
        return '<applicant {}, message {}>'.format(self.applicant_id, self.message)
    def set_applicant_id(self, id):
        self.applicant_id = id
    def set_employer_id(self, id):
        self.employer_id = id