from app.books import book_blueprint
from app.models import Books
from flask_restful import  Resource , Api ,fields ,marshal_with

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


