
#Chiffrement AES de données sensibles

from Crypto.Cipher import AES
import base64
import os

# Clé secrète (doit être 16, 24 ou 32 octets)
SECRET_KEY = os.getenv('AES_KEY', '16bytessecretkey')

def pad(s):
    return s + (16 - len(s) % 16) * chr(16 - len(s) % 16)

def unpad(s):
    return s[:-ord(s[len(s) - 1:])]

def encrypt(data):
    cipher = AES.new(SECRET_KEY.encode('utf-8'), AES.MODE_ECB)
    padded = pad(data)
    encrypted = cipher.encrypt(padded.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt(data):
    cipher = AES.new(SECRET_KEY.encode('utf-8'), AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(data))
    return unpad(decrypted.decode('utf-8'))
