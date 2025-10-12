from tmaqn2b.model.books import Book
from tmaqn2b.model.users import User
from tmaqn2b import db
from datetime import date, timedelta


class Loan(db.Document):
    meta = {"collection": "bookLoans"}
    member = db.ReferenceField(User)
    book = db.ReferenceField(Book)
    borrowDate = db.DateField()
    returnDate = db.DateField()
    renewCount = db.IntField()

    
    @staticmethod
    def getLoanByUser(email):
        loans = Loan.objects(member = User.getUser(email))
        sorted_loans = loans.order_by("-borrowDate", "returnDate")
        return sorted_loans
    
    @staticmethod
    def getLoanbyBook(email: str, title: str):
        book_doc = Book.get_book_by_title(title)

        if not book_doc:
            return None
        loans = Loan.objects(

            member = User.getUser(email),
            book = book_doc
        )
        sorted_loans = loans.order_by("returnDate")
        return sorted_loans.first()
    
    def renewLoan(self, new_date):
        self.borrowDate = new_date
        self.renewCount += 1
        self.save()

    def returnLoan(self, new_date):
        self.returnDate = new_date
        self.save()
        self.book.return_book()

    def deleteLoan(self):
        if self.returnDate:
            self.delete()

    def createLoan(member:User, book: Book, borrowDate, renewCount):
        latest_loan = Loan.getLoanbyBook(member.email, book.title)

        if not latest_loan or latest_loan.returnDate and book.available:
            loan = Loan(
                member = member,
                book = book,
                borrowDate = borrowDate,
                renewCount = renewCount,
            ).save()
            book.borrow_book()

            return loan
        
    def get_dueDate(self):
        return self.borrowDate + timedelta(days=14)

    def is_overdue(self):
        if not self.returnDate:
            return date.today() > self.get_dueDate()
        return False