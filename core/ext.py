from flask_login import LoginManager
from flask_mongoengine import MongoEngine, MongoEngineSessionInterface


login_manager = LoginManager()
db = MongoEngine()
session_interface = MongoEngineSessionInterface(db)
