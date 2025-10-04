from flask import Blueprint, render_template, request, url_for, redirect
from model.books import all_books

bp = Blueprint('book_bp', __name__) 

@bp.route('/')
@bp.route('/booktitles', methods=['GET'])
def show_base():
    # 1. Get the selected category from the URL query parameters.
    selected_category = request.args.get('category', 'All')

    # 2. Start with all books, sorted alphabetically by title
    sorted_books = sorted(all_books, key=lambda book: book['title'])
    
    # 3. Filter the books based on the selected category
    if selected_category != 'All':
        filtered_books = [
            book for book in sorted_books 
            if book['category'] == selected_category
        ]
    else:
        # If 'All' is selected, use the full sorted list
        filtered_books = sorted_books
        
    # 4. Pass the filtered list AND the selected category to the template
    return render_template(
        'books.html', 
        books=filtered_books, 
        panel='Book Titles',
        selected_category=selected_category
    )

@bp.route('/bookdetails', methods=['GET'])
def show_details():
    book_title = request.args.get('title')
    selected_book = next((book for book in all_books if book['title'] == book_title), None)
    
    if selected_book is None:
        # Use 'book_bp.show_base' to correctly reference the route on the Blueprint
        return redirect(url_for('book_bp.show_base')) 

    return render_template(
        'books_details.html',
        book=selected_book,
        panel='Book Details'
    )