from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func


db = SQLAlchemy()



class Books(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    image = db.Column(db.String, nullable=True)
    price = db.Column(db.Integer)
    no_of_pages = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=func.now())


    def __str__(self):
        return f"{self.title}"


    @classmethod
    def get_all_objects(cls):
        return cls.query.all()