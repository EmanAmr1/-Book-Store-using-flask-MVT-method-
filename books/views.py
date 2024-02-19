from flask import render_template
from app.models import Books

def books_index():
    books=Books.get_all_objects()
    return render_template("books/index.html",books=books)

