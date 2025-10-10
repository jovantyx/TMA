from model.books import Book
from model.users import User
from tmaqn2b import db
from datetime import date, timedelta

class Loan(db.Document):
    meta = {"collection": "bookLoans"}
    member = db.ReferenceField(User)
    book = db.ReferenceField(Book)
    borrowDate = db.DateField()
    returnDate = db.DateField()
    renewCount = db.IntField()

   