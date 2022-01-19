#!flask/bin/python 
from flask import Flask 
 
app = Flask(__name__) 


from api.book import book_api

app.register_blueprint(book_api)

@app.route('/')
def hello_world():
    return 'This is my first API call!'
 