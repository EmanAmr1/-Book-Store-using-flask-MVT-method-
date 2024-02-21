from app.categories import category_blueprint

@category_blueprint.route('/home' , methods=['GET'], endpoint='home')
def category_home():
    return "<h1>welcome to category home</h2>"




