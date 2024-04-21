import os
import sqlalchemy as sa
from config import Config
from flask_migrate import upgrade

def create_db():
    if (os.path.exists(Config.OS_DB_PATH)):
        print("DataBase already exists")
    else:
        open("app.db", "x")
    
def init_db(db):
    upgrade(Config.MIGRATIONS)
    
