from flask import render_template
from app.models import Books
from app.books import book_blueprint

@book_blueprint.route('',endpoint='books_index')
def books_index():
    books=Books.get_all_objects()
    return render_template("books/index.html",books=books)

