from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from security.auth import token_required
from utils.db import get_db
from utils.password import check_password

auth_bp = Blueprint('auth', __name__)
chat_bp = Blueprint('chat_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE email=%s", (data['email'],))
    if cur.fetchone():
        return jsonify({'error': 'Email existe déjà'}), 409
    hashed_pw = generate_password_hash(data['mot_de_passe'])
    cur.execute("INSERT INTO users (nom, prenom, email, telephone, mot_de_passe, role) VALUES (%s,%s,%s,%s,%s,%s)",
        (data['nom'], data['prenom'], data['email'], data['telephone'], hashed_pw, data['role']))
    conn.commit()
    return jsonify({'message': 'Utilisateur inscrit'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, mot_de_passe FROM users WHERE email=%s", (data['identifier'],))
    user = cur.fetchone()
    if user and check_password_hash(user[1], data['mot_de_passe']):
        token = jwt.encode({'user_id': user[0], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                           key='votre_clé_secrète', algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'error': 'Identifiants incorrects'}), 401

