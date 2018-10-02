from flask import Flask, jsonify, request, make_response
from app.models.database import DatabaseConnection

db = DatabaseConnection()
app = Flask(__name__)


@app.route('/auth/signup', methods=['POST'])
def create_user():
    data = request.get_json()
    user_name = data['user_name']
    email = data['email']
    user_password = data['user_password']
    if db.create_user(user_name, email, user_password) == "user_name already exists use another username":
        return jsonify({'message':'user_name already exists use another username'}), 400
    return jsonify({'message':'User created'}), 201

@app.route('/auth/login', methods=['POST'])
def login():
    return''

if __name__ =='__main__':
    app.run(port= 5000, debug= True)