from flask import Flask, jsonify
from flask_cors import CORS

DEBUG = True
# app 인스턴스화
app = Flask(__name__)
app.config.from_object(__name__)
# Cross Origin 설정
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


if __name__ == '__main__':
    app.run()
