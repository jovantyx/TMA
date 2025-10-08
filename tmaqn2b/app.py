from tmaqn2b import app, db
from tmaqn2b.controllers.bookController import bp as book_bp


app.register_blueprint(book_bp)