from flask import Flask, jsonify, request, make_response
from app.models.database import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from app.orders.models import Users

db = DatabaseConnection()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'keren'

@app.route('/orders/<order_id>', methods=['PUT'])
def update_an_order(order_id):
    data = request.get_json()
    order_status = data['order_status']
    db.update_order_status(order_status, order_id)
    return jsonify({'message': order_status}), 201


@app.route('/orders/<order_id>', methods=['GET'])
def get_an_order(order_id):
    order = db.get_an_order(order_id)
    if not order:
        return jsonify({'message': 'No order placed by that id'}), 400
    return jsonify({'message': order}), 200
    return order


@app.route('/orders', methods=['GET'])
def get_orders():
    order = db.get_all_orders()
    if not order:
        return jsonify({'message': 'No order found'}), 400
    return jsonify({'message': order}), 200


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
    db.create_order(user_id, menu_id, contact, quantity, order_status)
    return jsonify({'message': 'Order created'}), 201

    # if not contact == type(int):
    #     return jsonify({'Error': 'Contact has to be an integer'}), 400
    # if contact.strip() == '':
    #     return jsonify({'Error': 'Contact can not be empty'}), 400
    # if not len(contact) == 9:
    #     return jsonify({'Error': 'Contact has 9 integers'}), 400

    # if not quantity == type(int):
    #     return jsonify({'Error': 'quantity has to be an integer'}), 400
    # if quantity.strip() == '':
    #     return jsonify({'Error': 'quantity can not be empty'}), 400


@app.route('/menu', methods=['POST'])
def add_a_menu():
    data = request.get_json()
    menu_item = data['menu_item']
    price = data['price']
    db.create_menu(menu_item, price)
    # return jsonify({'message': 'Menu item added successfully'}), 201
    # if menu_item.strip() == '':
    #     return jsonify({'Error': 'menu_item can not be empty'}), 400

    # if price != type(int):
    #     return jsonify({'Error': 'price has to be an integer'}), 400
    # if price.strip() == '':
    #     return jsonify({'Error': 'price can not be empty'}), 400


@app.route('/menu', methods=['GET'])
def get_menu():
    menu = db.get_menu()
    if not menu:
        return jsonify({'message': 'No menu found'}), 400
    return jsonify({'message': menu}), 200


@app.route('/auth/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data['user_name']
    email = data['email']
    user_password = generate_password_hash(data['user_password'])

    if not data:
        return jsonify({'Erorr': 'Please enter all details to signup'})
    if user_name.strip() == '':
        return jsonify({'Erorr': 'username should not be empty'})

    if len(user_name) < 3:
        return jsonify({'Erorr': 'username is too short'})
    if email.strip() == '':
        return jsonify({'Erorr': 'email should not be empty'})
    if user_password.strip() == '':
        return jsonify({'Erorr': 'password can not be empty'})
    if not type(user_password) == str:
        return jsonify({'Erorr': 'password should be a string'})
    if len(user_password) < 9:
        return jsonify({'Erorr': 'password is too short'})

    if db.create_user(user_name, email, user_password) == "username exists":
        return jsonify({'message': 'username exists'}), 400
    return jsonify({'message': 'User created'}), 201


@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    user_name = data['user_name']
    user_password = data['user_password']
    db_user = db.get_a_user('user_name', user_name)

    if not db_user:
        return jsonify({'Error': 'No such user'}), 400
    user = Users(db_user[0], db_user[1], db_user[2], db_user[3], db_user[4])

    if user.user_name == user_name and check_password_hash(user.password, user_password):
        token = jwt.encode({'user_name': user.user_name, 'is_admin': user.is_admin,

                            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
                           app.config['SECRET_KEY'])
        return jsonify({'token': token.decode('UTF-8'), 'message': 'User logged-in'}), 200
    return jsonify({'Error': 'Please check your details'})
