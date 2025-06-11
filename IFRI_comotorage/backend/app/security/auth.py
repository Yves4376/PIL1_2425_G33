
#Gestion des JWT

import jwt
import os
from flask import request, jsonify
from functools import wraps
from datetime import datetime, timedelta

SECRET_KEY = os.getenv('SECRET_KEY', 'mon_secret_key')

def generate_jwt(user_id, role):
    payload = {
        'user_id': user_id,
        'role': role,
        'exp': datetime.utcnow() + timedelta(hours=24)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

def decode_jwt(token):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'error': 'Token requis'}), 401
        decoded = decode_jwt(token)
        if not decoded:
            return jsonify({'error': 'Token invalide ou expiré'}), 403
        return f(decoded, *args, **kwargs)
    return wrapper
