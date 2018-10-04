from flask import Flask, jsonify, request, make_response
from app.models.database import DatabaseConnection

db = DatabaseConnection()
app = Flask(__name__)


@app.route('/users/orders', methods=['POST'])
def make_an_order():
    data = request.get_json()
    if not data:
        return jsonify({'Error': 'Please fill in the neccssary data'}), 400
    user_id = data['user_id']
    menu_id = data['menu_id']
    contact = data['contact']
    quantity = data['quantity']
    order_status = data['order_status']
    if not contact == type(int):
        return({'Error': 'Contact has to be an integer'}), 400
    if contact.strip() == '':
        return({'Error': 'Contact can not be empty'}), 400
    if not len(contact) == 9:
        return({'Error': 'Contact has 9 integers'}), 400

    if not quantity == type(int):
        return({'Error': 'quantity has to be an integer'}), 400
    if quantity.strip() == '':
        return({'Error': 'quantity can not be empty'}), 400

    db.create_order(user_id, menu_id, contact, quantity, order_status)
    return jsonify({'message': 'Order created'}), 201


@app.route('/orders/<order_id>', methods=['GET'])
def get_an_order(order_id):
    order = db.get_an_order(order_id)
    if not order:
        return jsonify({'message': 'No order placed by that id'}), 400
    return jsonify({'message': order}), 200
    return 'one order'


@app.route('/orders/', methods=['GET'])
def get_orders():
    orders = db.get_all_orders()
    if not orders:
        return jsonify({'message': 'No orders made'}), 400
    return jsonify({'message': orders}), 200


@app.route('/orders/<order_id>', methods=['PUT'])
def update_an_order(order_id):
    data = request.get_json()
    order_status = data['order_status']
    db.update_order_status(order_status, order_id)
    return jsonify({'message': order_status})


@app.route('/menu', methods=['GET'])
def get_menu():
    menu = db.get_menu()
    if not menu:
        return jsonify({'message': 'No menu found'}), 400
    return jsonify({'message': menu}), 200


@app.route('/menu', methods=['POST'])
def add_a_menu():
    data = request.get_json()
    menu_item = data['menu_item']
    price = data['price']

    if not menu_item == type(str):
        return({'Error': 'menu_item has to be a string'}), 400
    if menu_item.strip() == '':
        return({'Error': 'menu_item can not be empty'}), 400

    if not price == type(int):
        return({'Error': 'price has to be a string'}), 400
    if price.strip() == '':
        return({'Error': 'price can not be empty'}), 400
    db.create_menu(menu_item, price)
    return jsonify({'message': 'Menu item added successfully'}), 201
