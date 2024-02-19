from flask import Blueprint

#books= Blueprint('')

book_blueprint= Blueprint("books",__name__,url_prefix="/books")

from app.books import  views