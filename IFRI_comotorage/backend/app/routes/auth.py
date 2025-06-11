
   #Authentification (inscription + connexion).

from flask import Blueprint, request, jsonify
from app import db
from app.models.user import User
from app.utils.password import hash_password, verify_password
from app.security.auth import generate_jwt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    champs = ['nom', 'prenom', 'email', 'telephone', 'mot_de_passe', 'role']
    if not all(field in data for field in champs):
        return jsonify({'error': 'Champs manquants'}), 400

    if User.query.filter((User.email == data['email']) | (User.telephone == data['telephone'])).first():
        return jsonify({'error': 'Email ou téléphone déjà utilisé'}), 409

    user = User(
        nom=data['nom'],
        prenom=data['prenom'],
        email=data['email'],
        telephone=data['telephone'],
        mot_de_passe=hash_password(data['mot_de_passe']),
        role=data['role']
    )
    db.session.add(user)
    db.session.commit()

    return jsonify({'message': 'Inscription réussie'}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    identifiant = data.get('email') or data.get('telephone')
    mot_de_passe = data.get('mot_de_passe')

    user = User.query.filter(
        (User.email == identifiant) | (User.telephone == identifiant)
    ).first()

    if not user or not verify_password(mot_de_passe, user.mot_de_passe):
        return jsonify({'error': 'Identifiants invalides'}), 401

    token = generate_jwt(user.id, user.role)
    return jsonify({'token': token}), 200
