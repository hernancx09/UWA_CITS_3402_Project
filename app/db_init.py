import os
from config import Testing
from flask_migrate import upgrade

def create_db(config_class):
    if not(config_class==Testing):
        if (os.path.exists(config_class.OS_DB_PATH)):
            print("DataBase already exists")
        else:
                open("app.db", "x")
    
def init_db(config_class):
    upgrade(config_class.MIGRATIONS)
    
