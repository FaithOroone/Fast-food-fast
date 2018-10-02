from flask import Flask
from database import DatabaseConnection

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
    return 'get the menu'

@app.route('/menu', methods=['POST'])
def add_a_menu():
    return 'add an item in the menu'

if __name__ =='__main__':
    app.run(port=5000, debug=True)