
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from dotenv import load_dotenv

# Chargement des variables d'environnement (.env)
load_dotenv()

# Création de l'objet SQLAlchemy global
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configuration sécurisée de l'application
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL',
        'mysql+pymysql://root:password@localhost/ifri_comotorage'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialisation des extensions
    db.init_app(app)
    CORS(app)

    # Importation des routes
    from app.routes.auth import auth_bp
    from app.routes.matching import matching_bp
    from app.routes.chat import chat_bp

    # Enregistrement des blueprints (groupes de routes)
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(matching_bp, url_prefix='/api/match')
    app.register_blueprint(chat_bp, url_prefix='/api/chat')

    return app
