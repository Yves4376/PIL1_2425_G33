import jwt
from flask import request, jsonify
from functools import wraps
from datetime import datetime, timedelta
from flask import current_app


SECRET = 'votre_clé_secrète'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token requis'}), 403
        try:
            data = jwt.decode(token.split()[1], SECRET, algorithms=['HS256'])
        except:
            return jsonify({'message': 'Token invalide'}), 403
        return f(data['user_id'], *args, **kwargs)
    return decorated


def generate_token(user_id):
    payload = {
        'sub': user_id,
        'exp': datetime.utcnow() + timedelta(hours=1)
    }
    return jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')

def verify_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return None