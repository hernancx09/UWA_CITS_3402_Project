from app import create_app
from config import Config

app = create_app(config_class=Config)
