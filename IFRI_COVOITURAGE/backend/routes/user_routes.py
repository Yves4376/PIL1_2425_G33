from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models.user import User
from extensions import db, bcrypt

user_bp = Blueprint('user_bp', __name__)
@user_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    new_user = User(email=data['email'], password=hashed_pw, name=data['name'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Utilisateur créé avec succès"}), 201

@user_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"message": "Email ou mot de passe incorrect"}), 401

user_bp = Blueprint('user_bp', __name__)
@user_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data['email']
    password = data['password']
    # vérifie user et retourne un JWT par exemple
    