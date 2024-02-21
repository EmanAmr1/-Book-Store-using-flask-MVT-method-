from flask_wtf import FlaskForm
from wtforms import  StringField,IntegerField
from wtforms.validators import DataRequired

class BookForm(FlaskForm):
    title = StringField('Title' , validators=[DataRequired()])
    image = StringField('Image' )
    price = IntegerField('Price' , validators=[DataRequired()])
    no_of_pages = IntegerField('No of pages' , validators=[DataRequired()])



