from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True
# app 인스턴스화
app = Flask(__name__)
app.config.from_object(__name__)
# Cross Origin 설정
CORS(app, resources={r'/*': {'origins': '*'}})


# Books list 추가
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET'])
def all_books():
    return jsonify({
        'status': 'success',
        'books': BOOKS
    })


if __name__ == '__main__':
    app.run()
