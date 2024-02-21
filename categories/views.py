from flask import render_template
from app.categories import category_blueprint
from app.models import Category
from app.categories.forms import CategoryForm
from flask import request ,redirect ,url_for

@category_blueprint.route('/home' , methods=['GET'], endpoint='home')
def category_home():
    return "<h1>welcome to category home</h2>"

@category_blueprint.route('/', methods=['GET'] ,endpoint='index')
def category_index():
    categories= Category.get_all_categories()
    return render_template('categories/index.html', categories=categories)



@category_blueprint.route("/createcategory", methods=['GET', 'POST'], endpoint='createcategory')
def create_category_viaform():
    form =CategoryForm(request.form)
    if request.method == 'POST' and form.validate():
        category_data = request.form.to_dict()  # Convert ImmutableMultiDict to dict
        if 'csrf_token' in category_data:
            del category_data['csrf_token']  # Exclude csrf_token from the data
        book = Category.save_category(category_data)
        return redirect(url_for('categories.index'))

    return render_template("categories/createcategory.html", form=form)

