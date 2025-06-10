import pytest
import os
import jwt
from datetime import datetime, timedelta
from app.utils.password import hash_password, verify_password
from app.security.encryption import encrypt_data, decrypt_data
from app.security.geo_utils import is_nearby

SECRET_KEY = os.getenv("SECRET_KEY")

def test_password_utils():
    pwd = "strong_pwd123"
    hashed = hash_password(pwd)
    assert verify_password(pwd, hashed)
    assert not verify_password("wrong", hashed)

def test_encryption():
    original = "hello world"
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original

def test_geo_utils():
    assert is_nearby(6.367, 2.418, 6.368, 2.419)  # Cotonou, très proche
    assert not is_nearby(6.367, 2.418, 9.345, 2.632)  # Cotonou vs Parakou

def test_jwt_token():
    payload = {"user_id": 1, "exp": datetime.utcnow() + timedelta(seconds=5)}
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    decoded = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    assert decoded["user_id"] == 1