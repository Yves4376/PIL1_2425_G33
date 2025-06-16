import jwt
from flask import request, jsonify
from functools import wraps

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