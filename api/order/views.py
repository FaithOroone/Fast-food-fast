from flask import Flask, request, json, jsonify
from modules import Order, OrderList

app = Flask(__name__)
#order = Order()
lst = OrderList()

#add an order endpoint
app = Flask(__name__)
@app.route('/api/v1/orders', methods=['POST'])
def add_an_order():
    if request.get_json():
        new_order_data = request.get_json()
        lst.orderlist.append(new_order_data)
        return jsonify({'new_order':new_order_data}), 200

#get all orders endpoint.
@app.route('/api/v1/orders', methods=['GET'])
def get_all_orders():
    return jsonify({'orders':lst.get_orders()}),200

#get a signal order endpoint
@app.route('/api/v1/orders/<int:orderId>', methods=['GET'])
def get_an_order(orderId):
    for order in lst.get_orders():
        if order['orderId']==orderId:
            return jsonify({'order':order}), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)