# from flask import Flask, request, jsonify
# import json
# from flask_cors import CORS


# app = Flask(__name__)
# CORS(app)  # Allow all origins (Consider restricting this in production)

# # Load user credentials from a JSON file
# def load_users():
#     with open("users.json", "r") as file:
#         return json.load(file)

# # Load home screen data from JSON file
# def load_home_data():
#     with open("home_data.json", "r") as file:
#         return json.load(file)

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.json
#     users = load_users()

#     email = data.get("email")
#     password = data.get("password")

#     for user in users:
#         if user["email"] == email and user["password"] == password:
#             return jsonify({"status": "success", "message": "Login successful"})
    
#     return jsonify({"status": "error", "message": "Invalid credentials"}), 401

# @app.route('/home', methods=['GET'])
# def home():
#     return jsonify(load_home_data())

# if _name_ == '_main_':
#     app.run(debug=True)

from flask import Flask, request, jsonify
import json
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Allow all origins (Consider restricting this in production)

def load_users():
    with open("users.json", "r") as file:
        return json.load(file)
        
# Load home screen data from JSON file
def load_home_data():
    with open("home_data.json", "r") as file:
        return json.load(file)

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    users = load_users()
    for user in users:
        if user["email"] == email and user["password"] == password:
            return jsonify({"message": "Login successful"}), 200

    return jsonify({"error": "Invalid email or password"}), 401

@app.route('/home', methods=['GET'])
def home():
    return jsonify(load_home_data())

if __name__ == '__main__':
    app.run()
