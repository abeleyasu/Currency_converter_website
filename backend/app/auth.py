from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    # Add authentication logic here
    return jsonify({"message": "Logged in successfully"})
    
@auth_bp.route('/register', methods=['POST'])
def register():
    # Add registration logic here
    return jsonify({"message": "Registered successfully"})
