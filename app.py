from flask import Blueprint, render_template, request, jsonify, url_for, redirect, Flask
from books import all_books

app = Flask(__name__)

@app.route('/')
@app.route('/booktitles', methods=['GET'])
def show_base():
    # 1. Get the selected category from the URL query parameters.
    #    Default to 'All' if no category is provided (first load or no search)
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
        panel='BOOK TITLES',
        selected_category=selected_category # Used to keep the dropdown selected
    )