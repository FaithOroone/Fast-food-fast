from flask import Flask, jsonify, request, make_response
from app.models.database import DatabaseConnection

db = DatabaseConnection()
app = Flask(__name__)
@app.route('/users/orders', methods=['POST'])
def make_an_order():
    return 'order placed'

@app.route('/users/orders', methods=['GET'])
def get_order_history():
    return 'history of orders'

@app.route('/orders/<orderId>', methods=['GET'])
def get_an_order():
    return 'one order'

@app.route('/orders/', methods=['GET'])
def get_orders():
    return 'list of order'

@app.route('/orders/<orderId>', methods=['PUT'])
def update_an_order():
    return 'update_an_order'

@app.route('/menu', methods=['GET'])
def get_menu():
    menu = db.get_menu()
    return jsonify({'message': menu})

@app.route('/menu', methods=['POST'])
def add_a_menu():
    data = request.get_json()
    menu_item = data['menu_item']
    price = data['price']
    db.create_menu(menu_item, price)
    return jsonify({'message':'Menu item added successfully'})

if __name__ =='__main__':
    app.run(port=5000, debug=True)
