from flask_restful import  reqparse

books_parser = reqparse.RequestParser()
books_parser.add_argument('title', type=str , required=True ,help="this is required" )
books_parser.add_argument('image', type=str  )
books_parser.add_argument('price', type=int , required=True ,help="this is required" )
books_parser.add_argument('no_of_pages', type=int , required=True ,help="this is required" )
books_parser.add_argument('category_id', type=int  )
