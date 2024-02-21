from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func
from flask import  url_for

db = SQLAlchemy()

class Category(db.Model):
    __tablename__='categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String, unique=True)
    categories = db.relationship('Books' , backref="categories", lazy= True)

    def __str__(self):
        return f"{self.name}"

    @classmethod
    def get_all_categories(cls):
        return cls.query.all()

    @classmethod
    def get_category_by_id(cls, id):
        return cls.query.get_or_404(id)

class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer)
    no_of_pages = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=func.now())
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)


    def __str__(self):
        return f"{self.title}"


    @classmethod
    def get_all_objects(cls):
        return cls.query.all()

    @classmethod
    def get_book_by_id(cls,id):
        return cls.query.get_or_404(id)



    @property
    def image_url(self):
        return url_for('static',filename=f'books/images/{self.image}')


    @property
    def show_url(self):
        return url_for("books.books_show",id=self.id)


    @classmethod
    def save_book(cls ,request_data):
        book = cls(**request_data)
        db.session.add(book)
        db.session.commit()
        return book

    @staticmethod
    def update_book(book, form_data):
        try:
            # Update the book's information
            book.title = form_data.get('title')
            book.image = form_data.get('image')
            book.price = form_data.get('price')
            book.no_of_pages = form_data.get('no_of_pages')
            db.session.commit()
            return True
        except KeyError:
            db.session.rollback()  # Rollback changes in case of error
            return False

