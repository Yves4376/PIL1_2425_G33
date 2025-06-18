from flask import Flask, send_from_directory, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_bp
from routes.chat import chat_bp, db
from routes.matching import matching_bp
from flask_socketio import emit
import os
from flask_cors import CORS




app = Flask(__name__)

CORS(app)  # Autorise les appels frontend vers l'API

app.config['SECRET_KEY'] = 'votre_clé_secrète'
app.cofig['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/nom_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

# Enregistrement des blueprints
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(chat_bp, url_prefix='/api')
app.register_blueprint(matching_bp, url_prefix='/api')

# 📁 Chemin absolu vers le dossier frontend/
FRONTEND_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'frontend'))

# 🎯 Route pour la page d'accueil
@app.route('/')
def serve_index():
    return send_from_directory(FRONTEND_FOLDER, 'index.html')

# 🎯 Route pour tous les autres fichiers (CSS, JS, images...)
@app.route('/<path:filename>')
def serve_static_file(filename):
    return send_from_directory(FRONTEND_FOLDER, filename)

# 📡 Exemple d'API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    # ➕ ici ta logique de connexion
    return jsonify({"message": "Connexion réussie", "token": "1234.jwt.token"})

if __name__ == '__main__':
    app.run(debug=True)
    db.init_app(app)
