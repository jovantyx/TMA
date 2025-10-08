from tmaqn2b import app, db
from tmaqn2b.controllers.bookController import bp as book_bp
from tmaqn2b.controllers.auth import auth
from flask import render_template

app.register_blueprint(book_bp)
app.register_blueprint(auth)
