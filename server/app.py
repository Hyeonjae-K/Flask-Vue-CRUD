import uuid

from flask import Flask, jsonify, request
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
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


# BOOKS에 book_id와 같은 id를 갖는 딕셔너리가 있을 경우 삭제
def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# json 형식으로 'pong!' 반환
# jsonify == 데이터 타입을 json으로 변경
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    # response_object에 {'status': 'success'}인 키 벨류를 갖는 딕셔너리 저장
    response_object = {'status': 'success'}
    # 요청이 POST일 경우
    if request.method == 'POST':
        # 새로 추가할 데이터인 json형태의 body를 post_data에 저장
        # Dictionary 형태로 저장됨
        post_data = request.get_json()
        # 전달받은 데이터를 BOOKS에 추가
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        # response_object에 {'message': 'Book added!'}인 키 벨류 추가
        response_object['message'] = 'Book added!'
    # 요청이 POST가 아닐 경우(GET)
    else:
        # response_object에 {'books': BOOKS}인 키 벨류 추가
        response_object['books'] = BOOKS
    # response_object를 json형태로 반환
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    # response_object에 {'status': 'success'}인 키 벨류를 갖는 딕셔너리 저장
    response_object = {'status': 'success'}
    # 요청이 PUT일 경우
    if request.method == 'PUT':
        # 수정된 데이터인 json형태의 body를 post_data에 저장
        # Dictionary 형태로 저장됨
        post_data = request.get_json()
        # id를 통해 수정 전 데이터를 BOOKS에서 삭제
        remove_book(book_id)
        # 수정 후 데이터를 BOOKS에 추가
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        # response_object에 {'message': 'Book updated!'}인 키 벨류 추가
        response_object['message'] = 'Book updated!'
    # 요청이 DELETE일 경우
    elif request.method == 'DELETE':
        # id를 통해 해당 데이터를 BOOKS에서 삭제
        remove_book(book_id)
        # response_object에 {'message': 'Book removed!'}인 키 벨류 추가
        response_object['message'] = 'Book removed!'
    # response_object를 json형태로 반환
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
