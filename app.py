from flask import Blueprint, render_template, request, jsonify, url_for, redirect, Flask
from controllers.bookController import bp as book_bp

app = Flask(__name__)

app.register_blueprint(book_bp)