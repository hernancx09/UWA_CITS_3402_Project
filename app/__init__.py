from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db_init import init_db, create_db

db = SQLAlchemy()
migrate = Migrate()
    
def create_app(config_class):
    app = Flask(__name__, 
                static_url_path='',
                static_folder='static')
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        create_db(config_class)
        init_db(config_class)
        from app import routes, models
    return app



