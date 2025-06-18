from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models.User import User
from extensions import db, bcrypt

@user_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], password=hashed_pw, name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Utilisateur créé avec succès"}), 201

user_bp = Blueprint('user_bp', __name__)
@user_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    # vérifie user et retourne un JWT par exemple
    