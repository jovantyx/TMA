from flask import Blueprint, render_template, request, jsonify, url_for, redirect, Flask
from books import all_books

app = Flask(__name__)

@app.route('/')
@app.route('/booktitles', methods=['GET'])
def show_base():
    # 1. Sort the list of books alphabetically by title
    sorted_books = sorted(all_books, key=lambda book: book['title'])
    
    # 2. Pass the sorted list to the template
    return render_template('books.html', books=sorted_books, panel='BOOK TITLES')
