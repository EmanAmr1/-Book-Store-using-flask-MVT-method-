from flask import render_template ,request,redirect,url_for, make_response
from app.models import Books ,db
from app.books import book_blueprint
from app.books.forms import BookForm


@book_blueprint.route('',endpoint='books_index')
def books_index():
    books=Books.get_all_objects()
    return render_template("books/index.html",books=books)


@book_blueprint.route("/<int:id>" , endpoint="books_show")
def book_show(id):
    book= Books.get_book_by_id(id)
    return render_template("books/details.html" , book=book )


@book_blueprint.route("/create" ,methods=['GET','POST'] ,endpoint="create")
def create_book():
    if request.method == 'POST':
        book=Books.save_book(request.form)
        #return redirect(url_for('books.books_index'))
        return redirect(book.show_url)
    return render_template("books/create.html")


@book_blueprint.route("/delete_book/<int:id>" , methods=['POST'])
def delete_book(id):
    # Get the book object from the database
    book = Books.get_book_by_id(id)
    # Delete the book from the database
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('books.books_index'))


@book_blueprint.route('/update_book/<int:id>', methods=['GET', 'POST'], endpoint="book_update")
def update_book(id):
    # Get the book object from the database
    book = Books.get_book_by_id(id)

    if request.method == 'POST':
        if Books.update_book(book, request.form):
            return redirect(url_for('books.books_index'))
        else:
            return redirect(request.url)

    # Render the template with the book data
    return render_template("books/update.html", book=book)


@book_blueprint.route("/createform" , methods=['GET' , 'POST'], endpoint='createform')
def create_book_viaform():
    form=BookForm()
    return render_template("books/createform.html" , form=form)


@book_blueprint.errorhandler(404)
def get_404(error):
    return render_template("error404.html")