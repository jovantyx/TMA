from flask import Flask
from controllers.bookController import bp as book_bp

app = Flask(__name__)

app.register_blueprint(book_bp)