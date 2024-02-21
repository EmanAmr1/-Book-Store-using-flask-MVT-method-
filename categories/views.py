from flask import render_template
from app.categories import category_blueprint
from app.models import Category


@category_blueprint.route('/home' , methods=['GET'], endpoint='home')
def category_home():
    return "<h1>welcome to category home</h2>"

@category_blueprint.route('/', methods=['GET'] ,endpoint='index')
def category_index():
    categories= Category.get_all_categories()
    return render_template('categories/index.html', categories=categories)





