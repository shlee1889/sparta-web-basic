from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')

@app.route('/order', methods=['GET'])
def listing():
    orders = list(db.orders.find({},{'_id': False}))
    return jsonify({'all_orders': orders})

## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def saving():
    name = request.form['name']
    quantity = request.form['quantity']
    address = request.form['address']
    tel = request.form['tel']

    doc = {
      'name': name,
      'quantity': quantity,
      'address': address,
      'tel': tel
    }

    db.orders.insert_one(doc)

    return jsonify({'msg':'저장이 완료되었습니다!'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)