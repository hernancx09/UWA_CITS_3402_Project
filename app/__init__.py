from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.db_init import init_db, create_db

app = Flask(__name__, 
            static_url_path='',
            static_folder='static')
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

create_db()
with app.app_context():
    init_db(db)

from app import routes, models


