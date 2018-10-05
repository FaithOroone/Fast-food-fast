from flask import Flask, jsonify, request, make_response
from app.models.database import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import jwt
import datetime
from app.orders.models import Users

db = DatabaseConnection()
app = Flask(__name__)
app.config['SECRET_KEY'] = 'keren'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message' : 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            db_user = db.get_a_user('user_name', data['user_name'])
            current_user = Users(db_user[0], db_user[1], db_user[2],
                            db_user[3], db_user[4])
            current_user.is_admin = data['is_admin']
        except:
            return jsonify({'message':'Token is invalid'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

#get order_history
@app.route('/users/orders/<int:user_id>', methods=['GET'])
@token_required
def get_order_history(current_user, user_id):
    history = db.get_order_history(user_id)
    return jsonify({'order_history' : history})

#update an order
@app.route('/orders/<int:order_id>', methods=['PUT'])
@token_required
def update_an_order(current_user, order_id,):
    data = request.get_json()
    order_status = data['order_status']
    db.update_order_status(order_status, order_id)
    return jsonify({'message': order_status}), 201

#get an order
@app.route('/orders/<int:order_id>', methods=['GET'])
@token_required
def get_an_order(current_user, order_id):
    order = db.get_an_order('order_id', order_id)
    if not order:
        return jsonify({'message': 'No order placed by that id'}), 400
    return jsonify({'message': order}), 200

#get all orders
@app.route('/orders', methods=['GET'])
@token_required
def get_orders(current_user):
    order = db.get_all_orders()
    if not order:
        return jsonify({'message': 'No order found'}), 400
    return jsonify({'message': order}), 200

#make an order
@app.route('/users/orders', methods=['POST'])
@token_required
def make_an_order(current_user):
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

#add a menu
@app.route('/menu', methods=['POST'])
@token_required
def add_a_menu(current_user):
    data = request.get_json()
    if not data:
        return jsonify({"Error":"Please fill in all the fields"}), 400
    menu_item = data['menu_item']
    price = data['price']

    if menu_item.strip() == '':
        return jsonify({'Error': 'menu_item can not be empty.'}),400

    if not menu_item:
        return jsonify({"Error":"menu_item is required."}), 400

    if menu_item.isnumeric():
        return jsonify({"Error":"menu_item can not be an integer!"}), 400

    if not price:
        return jsonify({"Error":"Price is required."}), 400

    db.create_menu(menu_item, price)
    return jsonify({'message': 'Menu item added successfully'}), 201

#get menu
@app.route('/menu', methods=['GET'])
@token_required
def get_menu(current_user):
    menu = db.get_menu()
    if not menu:
        return jsonify({'message': 'No menu found'}), 400
    return jsonify({'message': menu}), 200

#create user
@app.route('/auth/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'Error': 'Please enter all details to signup.'}),400
    user_name = str(data['user_name'])
    email = data['email']
    user_password = generate_password_hash(data['user_password'])

    if user_name.strip() == '':
        return jsonify({'Error': 'Username can not be empty.'}),400

    if not user_name:
        return jsonify({"Error":"Username is required."}), 400

    if user_name.isnumeric():
        return jsonify({"Error":"Username can not be an integer!"}), 400

    if len(user_name) < 3:
        return jsonify({'Error': 'Username is too short.'}),400

    if email.strip() == '':
        return jsonify({'Error': 'Email should not be empty'}), 400

    if user_password.strip() == '':
        return jsonify({'Error': 'Password can not be empty'}), 400

    if len(user_password) < 3:
        return jsonify({'Error': 'Password is too short'}),400

    if db.create_user(user_name, email, user_password) == "username exists":
        return jsonify({'message': 'username exists'}), 400
    return jsonify({'message': 'you have successfully signed up'}), 200

#login
@app.route('/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return({"message":"Please fill all the fields"})
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
