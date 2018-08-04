# -*- coding: utf-8 -*-
"""
Created on Sat Aug  4 10:14:37 2018

"""
from flask import Flask, jsonify, abort, request
import requests

app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello Steven'


stocks = [{
            'id': 1,
            'symbol': u'GOOG',
            'open': 1000.3,
            'exchange': u'NYSE',
            'done': False
        },{
            'id': 2,
            'symbol': u'APPL',
            'open': 210.3,
            'exchange': u'NYSE',
            'done': True
        }]

    
@app.route('/stocks', methods=['GET'])
def get_stocks():
    # get all from db
    # stocks = get_data_from_rdb()
    return jsonify({'stock': stocks})


@app.route('/stock/<int:s_id>', methods=['GET'])
def get_stock(s_id):
    stock = [s for s in stocks if s['id'] == s_id]
    print(stock)
    if len(stock) == 0:
        abort(404)
    return jsonify({'stock': stock[0]})

@app.route('/stocks', methods=['POST'])
def create_stock():
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
    result = requests.get('http://www.google.com').content
    # 3rd party ......
    # blahblahblah
    return result

if __name__ == '__main__':
    app.run()
