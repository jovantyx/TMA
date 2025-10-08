from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '495F33C48EEDD'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'books',
        'host': 'localhost',
        'port': 27017
    }
    db = MongoEngine(app) 
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Please login or register first to get an account."

    return app, db, login_manager

app, db, login_manager = create_app()