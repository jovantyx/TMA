from flask import Flask
from flask_mongoengine import MongoEngine

def create_app():
    app = Flask(__name__)
    app.config['SeCRET_KEY'] = 'your_secret_key'
    app.config['MONGODB_SETTINGS'] = {
        'db': 'books',
        'host': 'localhost',
        'port': 27017
    }
    db = MongoEngine(app) 

    return app, db

app, db = create_app()