from flask import Blueprint, render_template, request, url_for, redirect, flash
from tmaqn2b.model.books import Book
from tmaqn2b.model.forms import BookForm

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

@bp.route('/newbook', methods=['GET', 'POST'])
def new_book():
    form = BookForm()
    if request.method == 'POST':
        if form.validate():
            existing_book = Book.get_book_by_title(form.title.data)
            if not existing_book:
                authors= []

                if form.author_1.data:
                    if form.is_illustrator_1.data:
                        authors.append(f"{form.author_1.data} (Illustrator)")
                    else:
                        authors.append(form.author_1.data)

                if form.author_2.data:
                    if form.is_illustrator_2.data:
                        authors.append(f"{form.author_2.data} (Illustrator)")
                    else:
                        authors.append(form.author_2.data)
                
                if form.author_3.data:
                    if form.is_illustrator_3.data:
                        authors.append(f"{form.author_3.data} (Illustrator)")
                    else:
                        authors.append(form.author_3.data)

                if form.author_4.data:
                    if form.is_illustrator_4.data:
                        authors.append(f"{form.author_4.data} (Illustrator)")
                    else:
                        authors.append(form.author_4.data)
                    
                if form.author_5.data:
                    if form.is_illustrator_5.data:
                        authors.append(f"{form.author_5.data} (Illustrator)")
                    else:
                        authors.append(form.author_5.data)

                book = Book.create_book(
                    genres=form.genres.data,
                    title=form.title.data,
                    category=form.category.data,
                    url=form.url.data,
                    description=form.description.data.splitlines(),
                    authors=authors,
                    pages=form.pages.data,
                    available=form.copies.data,
                    copies=form.copies.data
                )
                flash(f'{book.title} added successfully!', 'success')
                return redirect(url_for('book_bp.new_book'))
            else:
                form.title.errors.append("Book with this title already exists.")
    return render_template('new_book.html', form=form, panel="Add New Book")