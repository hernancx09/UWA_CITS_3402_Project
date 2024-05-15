import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'GroupProject'
    OS_DB_PATH = os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + OS_DB_PATH
    MIGRATIONS = os.path.join(basedir, 'migrations')

class Testing:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'GroupProject'
    #use memory db
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite://'
    MIGRATIONS = os.path.join(basedir, 'migrations')