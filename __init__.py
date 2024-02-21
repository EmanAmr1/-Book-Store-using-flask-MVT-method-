

from flask import Flask
from app.config import config_options as AppConfig
from app.models import db
from flask_migrate import Migrate


def create_app(config_name="prd"):
    app = Flask(__name__)
    current_config = AppConfig[config_name]
    print(current_config)
    app.config['SQLALCHEMY_DATABASE_URI'] =current_config.SQLALCHEMY_DATABASE_URI
    app.config.from_object(current_config)
    db.init_app(app)
    migrate = Migrate(app, db ,render_as_batch=True)

    from app.books import book_blueprint
    app.register_blueprint(book_blueprint)

    from app.categories import  category_blueprint
    app.register_blueprint(category_blueprint)

    return app