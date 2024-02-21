from app.books import book_blueprint
from app.models import Books


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
