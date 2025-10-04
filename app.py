from flask import Blueprint, render_template, request, jsonify, url_for, redirect, Flask
from model.books import all_books

app = Flask(__name__)

@app.route('/')
@app.route('/booktitles', methods=['GET'])
def show_base():
    
    selected_category = request.args.get('category', 'All')

    sorted_books = sorted(all_books, key=lambda book: book['title'])
    
    if selected_category != 'All':
        filtered_books = [
            book for book in sorted_books 
            if book['category'] == selected_category
        ]
    else:
        filtered_books = sorted_books
        
    return render_template(
        'books.html', 
        books=filtered_books, 
        panel='BOOK TITLES',
        selected_category=selected_category 
    )

@app.route('/bookdetails', methods=['GET'])
def show_details():
    book_title = request.args.get('title')
    
    selected_book = next((book for book in all_books if book['title'] == book_title), None)
    
    if selected_book is None:
        return redirect(url_for('show_base'))

    return render_template(
        'books_details.html',
        book=selected_book,
        panel='BOOK DETAILS'
    )