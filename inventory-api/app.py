#!flask/bin/python 
from flask import Flask, jsonify 
 
app = Flask(__name__) 
 
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
 
@app.route('/inventory/api/v1.0/books', methods=['GET']) 
def get_books(): 
    return jsonify({'books': books}) 
 
if __name__ == '__main__': 
    app.run(debug=True)