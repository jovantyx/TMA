from flask import Blueprint, render_template, request, url_for, redirect
from tmaqn2b.model.books import Book

bp = Blueprint('book_bp', __name__) 

@bp.route('/')
@bp.route('/booktitles', methods=['GET'])
def show_books():
    if Book.objects.count() == 0:
        Book.save_books()
    all_books = Book.get_all_books()
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
        panel='Book Titles',
        selected_category=selected_category
    )

@bp.route('/bookdetails', methods=['GET'])
def show_details():
    book_title = request.args.get('title')
    selected_book = Book.get_book_by_title(book_title)
    
    if selected_book is None:
        return redirect(url_for('book_bp.show_books')) 

    return render_template(
        'books_details.html',
        book=selected_book,
        panel='Book Details'
    )