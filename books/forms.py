from flask_wtf import FlaskForm
from wtforms import  StringField,IntegerField
from wtforms.validators import DataRequired
from wtforms_sqlalchemy.fields import QuerySelectField
from app.models import Category

class BookForm(FlaskForm):
    title = StringField('Title' , validators=[DataRequired()])
    image = StringField('Image' )
    price = IntegerField('Price' , validators=[DataRequired()])
    no_of_pages = IntegerField('No of pages' , validators=[DataRequired()])
    category_id = QuerySelectField("Category" , query_factory=lambda:Category.get_all_categories())



