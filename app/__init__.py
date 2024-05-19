from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db_init import init_db, create_db
from flask_login import LoginManager
from sqlalchemy import MetaData

# naming conventions for sqlalchemy metadata
# Ensures no errors when trying to drop constraints without names
convention = {
  "ix": "ix_%(column_0_label)s",
  "uq": "uq_%(table_name)s_%(column_0_name)s",
  "ck": "ck_%(table_name)s_%(constraint_name)s",
  "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
  "pk": "pk_%(table_name)s"
}

db = SQLAlchemy(metadata=MetaData(naming_convention=convention))
migrate = Migrate()
login = LoginManager()

def create_app(config_class):
    app = Flask(__name__,
                static_url_path='',
                static_folder='static')
    #set config class
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)
    login.login_view = 'login'
    with app.app_context():
      #create and initialize db
        create_db(config_class)
        init_db(config_class)
        from app import routes, models
    return app



