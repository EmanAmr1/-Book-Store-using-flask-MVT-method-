from app.books import book_blueprint
from app.models import Books,db
from flask_restful import  Resource , Api ,fields ,marshal_with
from flask import request
from  app.books.parsers import books_parser

@book_blueprint.route("/api" , endpoint="api")
def get_books():
    books = Books.query.all()
    bks= []
    for bk in books:
        bk_data=bk.__dict__
        del bk_data["_sa_instance_state"]
        bks.append(bk_data)
        print(bks)
    return bks


category_serilizer = {
    "id": fields.Integer,
    "name": fields.String,
    "description":fields.String
}

book_serilizer = {
    "id":fields.Integer,
    "title":fields.String,
    "image":fields.String,
    "price":fields.Integer,
    " no_of_pages":fields.Integer,
    "category_id":fields.Integer,
    "category_name": fields.Nested(category_serilizer)
}


class BookList(Resource):
    @marshal_with(book_serilizer)
    def get(self):
        books= Books.query.all()
        return  books , 200

    @marshal_with(book_serilizer)
    def post(self):
        print(request.data)
        book_data = books_parser.parse_args()
        print(book_data)
        book = Books.save_book(book_data)
        return book , 201


class bookResource(Resource):
    @marshal_with(book_serilizer)
    def get(self ,bk_id):
        book= Books.get_book_by_id(bk_id)
        return book , 200

    @marshal_with(book_serilizer)
    def put(self,bk_id):
        book = Books.get_book_by_id(bk_id)
        if book:
            book_data = books_parser.parse_args()
            book.title=book_data['title']
            book.image = book_data['image']
            book.price = book_data['price']
            book.no_of_pages = book_data['no_of_pages']
            book.category_id = book_data['category_id']
            db.session.add(book)
            db.session.commit()
            return book




    def delete(self ,bk_id):
        delbook= Books.delete_book(bk_id)
        return delbook , 204