from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SelectMultipleField, SelectField, TextAreaField, IntegerField
from wtforms.validators import Email, Length, InputRequired, URL

class RegForm(FlaskForm):
    email = StringField('Email',  validators=[InputRequired(), Email(message='Invalid email'), Length(max=30)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=20)])
    name = StringField('Name')

class BookForm(FlaskForm):
    
    GENRE_CHOICES = [\
        ("Animals", "Animals"), ("Business", "Business"), ("Comics", "Comics"), \
        ("Communication", "Communication"), ("Dark Academia", "Dark Academia"), \
        ("Emotion", "Emotion"), ("Fantasy", "Fantasy"), ("Fiction", "Fiction"), \
        ("Friendship", "Friendship"), ("Graphic Novels", "Graphic Novels"), \
        ("Grief", "Grief"), ("Historical Fiction", "Historical Fiction"), \
        ("Indigenous", "Indigenous"), ("Inspirational", "Inspirational"), ("Magic", "Magic"),\
        ("Mental Health", "Mental Health"), ("Nonfiction", "Nonfiction"), ("Personal Development", "Personal Development"), \
        ("Philosophy", "Philosophy"), ("Picture Books", "Picture Books"), ("Poetry", "Poetry"), \
        ("Productivity", "Productivity"), ("Psychology", "Psychology"), ("Romance", "Romance"),\
        ("School", "School"), ("Self Help", "Self Help")\
    ]
    
    genres = SelectMultipleField("Choose multiple Genres:", 
                                 choices=GENRE_CHOICES,
                                 validators=[InputRequired()])

    title = StringField("Title", validators=[InputRequired()])

    category = SelectField("Choose a category:", choices=[
        "Adult", "Teens", "Children"
    ], validators=[InputRequired()])

    url = StringField("URL for Cover:", validators=[InputRequired(), URL()])

    description = TextAreaField("Description:", validators=[InputRequired()])

    author_1 = StringField("Author 1:", validators=[InputRequired()])

    is_illustrator_1 = BooleanField("Illustrator")

    author_2 = StringField("Author 2:")

    is_illustrator_2 = BooleanField("Illustrator")

    author_3 = StringField("Author 3:")

    is_illustrator_3 = BooleanField("Illustrator")
    
    author_4 = StringField("Author 4:")

    is_illustrator_4 = BooleanField("Illustrator")

    author_5 = StringField("Author 5:")

    is_illustrator_5 = BooleanField("Illustrator")

    pages = IntegerField("Number of pages:", validators=[InputRequired()])

    copies = IntegerField("Number of copies:", validators=[InputRequired()])