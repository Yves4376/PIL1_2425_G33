import os
import jwt
from datetime import datetime, timedelta
from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from dotenv import load_dotenv
from app.models.user import get_user_by_username

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = get_user_by_username(username)
    if user and check_password_hash(user.password, password):
        payload = {
            "user_id": user.id,
            "exp": datetime.utcnow() + timedelta(hours=1)
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return jsonify(token=token)

    return jsonify({"error": "Identifiants invalides"}), 401