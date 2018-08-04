from flask import Flask, jsonify
from flask import abort
from flask import request
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


stocks = [
    {
        'id': 1,
        'symbol': u'GOOG',
        'open': 1000.3,
        'exchange': u'NYSE',
        'done': False
    },
    {
        'id': 2,
        'symbol': u'APPL',
        'open': 210.3,
        'exchange': u'NYSE',
        'done': False
    }
]


@app.route('/stocks', methods=['GET'])
def get_tasks():
    return jsonify({'stocks': stocks})


@app.route('/stocks/<int:s_id>', methods=['GET'])
def get_task(s_id):
    stock = [s for s in stocks if stocks['id'] == s_id]
    if len(stock) == 0:
        abort(404)
    return jsonify({'stock': stock[0]})


@app.route('/stocks', methods=['POST'])
def create_task():
    if not request.json or not 'symbol' in request.json:
        abort(400)
    stock = {
        'id': stocks[-1]['id'] + 1,
        'symbol': request.json['symbol'],
        'open': request.json.get('open', ""),
        'exchange': request.json['exchange'],
        'done': False
    }
    stocks.append(stock)
    return jsonify({'stock': stock}), 201


@app.route('/url')
def get_data():
    return requests.get('http://127.0.0.1:5000/stocks').content


if __name__ == '__main__':
    app.run()
