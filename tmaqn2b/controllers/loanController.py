from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required, current_user
from tmaqn2b.model.loans import Loan
from tmaqn2b.model.books import Book
from tmaqn2b.model.users import User
from random import randint
from datetime import date, timedelta

loan_bp = Blueprint('loan_bp', __name__)


def generate_date(a: date, add_days: bool) -> date: 
    random_td = timedelta(days=randint(10, 20))
    
    if add_days:
        # This logic handles the renewal constraint from the original code
        if a >= date.today() - timedelta(days=10):
            return date.today()
        
        # New renewal/return date is today plus a random duration (10-20 days)
        return date.today() + random_td
    else:
        # New borrowDate is the start date (a, which is date.today()) minus a random duration
        # This calculates a past date, consistent with the original logic's intent.
        return a - random_td


@loan_bp.route('/loans')
def display_loans():
    if current_user.is_authenticated:
        user_loans = Loan.objects(member=current_user.id).order_by('-borrowDate')
        return render_template(
            'loans.html',
            all_loans=user_loans,
            panel='Current Loans',
        )
    else:
        flash("Please login or register first to get an account", "error")
        return redirect(url_for('auth.login'))
        

@loan_bp.route('/loans/renew_loan/<book_title>', methods=['POST'])
def renew_loan(book_title):
    
    loan = Loan.getLoanbyBook(current_user.email, book_title)
    
    new_borrowDate = generate_date(loan.borrowDate, True)
    loan.renewLoan(new_borrowDate)
    flash(f"{loan.book.title} loan has been renewed.", "success")
    return redirect(url_for('loan_bp.display_loans'))


@loan_bp.route('/loans/return_loan/<book_title>', methods=['POST'])
def return_loan(book_title):
    
    loan = Loan.getLoanbyBook(current_user.email, book_title)
    return_date = generate_date(loan.borrowDate, True)
    loan.returnLoan(return_date)
    flash(f"{loan.book.title} loan has been returned", "success")
    return redirect(url_for('loan_bp.display_loans'))



@loan_bp.route('/loans/delete_loan/<book_title>', methods=['POST'])
def delete_loan(book_title):
    
    loan = Loan.getLoanbyBook(current_user.email, book_title)
    new_borrowDate = generate_date(loan.borrowDate, True)
    loan.renewLoan(new_borrowDate)
    flash(f"{loan.book.title} loan has been renewed.", "success")
        
    return redirect(url_for('loan_bp.display_loans'))


@loan_bp.route('/make_loan/<book_title>', methods=['GET'])
def make_loan(book_title):
    if current_user.is_authenticated:
        book = Book.get_book_by_title(book_title)
        borrowDate = generate_date(date.today(), False)
        loan = Loan.createLoan(current_user, book, borrowDate, 0)
        if loan:
            flash(f"{loan.book.title} has been loaned.", "success")
        else:
            flash("Error creating loan", "error")
        return redirect(url_for("book_bp.show_books"))
    else:
        flash("Please login or register first to get an account", "error")
        return redirect(url_for('auth.login'))

