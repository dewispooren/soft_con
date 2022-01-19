from flask import Blueprint,request,jsonify

book_api = Blueprint('book', __name__, url_prefix='/inventory/api/v1.0/book')


books = [ 
    { 
        'id': 1, 
        'title': u'La Divina Commedia', 
        'author': u'Dante Alighieri',  
        'quantity': 3 
    }, 
    { 
        'id': 2, 
        'title': u'The sun also rises', 
        'description': u'Ernest Hemingway',  
        'quantity': 1 
    } 
] 
 
@book_api.route('/', methods=['GET']) 
def get_books(): 
    return jsonify({'books': books}) 


@book_api.route('/<book_id>', methods=['GET'])
def get_book_by_id(book_id=0):
    for book in books:
        if book['id'] == int(book_id):
            return jsonify({'book':book})
    return jsonify({'book':''})


@book_api.route('/<book_id>', methods=['DELETE'])
def delete_book_by_id(book_id=0):
    for book in books:
        if book['id'] == int(book_id):
            books.remove(book)
            return jsonify({'books': books}) 
    return jsonify({'books': books})
    

@book_api.route('/',methods=['POST'])
def create():
    data = request.get_json(force=True)
    books.append(data)
    return jsonify({'books': books}) 


