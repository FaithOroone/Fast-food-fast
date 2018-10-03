from flask import Flask, jsonify, request, make_response
from app.models.database import DatabaseConnection

db = DatabaseConnection()
app = Flask(__name__)


@app.route('/users/orders', methods=['POST'])
def make_an_order():
    data = request.get_json()
    if not data:
        return jsonify({'message': 'Please fill in the neccssary data'}), 400
    user_id = data['user_id']
    menu_id = data['menu_id']
    contact = data['contact']
    quantity = data['quantity']
    order_status = data['order_status']
    db.create_order(user_id, menu_id, contact, quantity, order_status)
    return jsonify({'message': 'Order created'}), 201



@app.route('/users/orders', methods=['GET'])
def get_order_history():
    return 'history of orders'


@app.route('/orders/<orderId>', methods=['GET'])
def get_an_order():
    return 'one order'


@app.route('/orders/', methods=['GET'])
def get_orders():
    orders = db.get_all_orders()
    if not orders:
        return jsonify({'message': 'No orders made'}), 400
    return jsonify({'message': orders}), 200

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
    db.create_menu(menu_item, price)
    return jsonify({'message': 'Menu item added successfully'}), 201


if __name__ =='__main__':
    app.run(port=5000, debug=True)
