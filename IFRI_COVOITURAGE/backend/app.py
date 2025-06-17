"""from flask import Flask
from routes.auth import auth_bp
from routes.chat import chat_bp
from routes.matching import matching_bp
from flask_cors import CORS

app = Flask(_name_)
CORS(app)
app.config['SECRET_KEY'] = 'votre_clé_secrète'

# Enregistrement des blueprints
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(chat_bp, url_prefix='/api')
app.register_blueprint(matching_bp, url_prefix='/api')

if _name_ == '_main_':
    app.run(debug=True) """



from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_socketio import SocketIO
from dotenv import load_dotenv
import os

from backend.utils.db import init_db
from backend.routes.auth import auth_bp
from backend.routes.chat import chat_bp
from backend.routes.matching import match_bp

# Initialisation des extensions
jwt = JWTManager()
socketio = SocketIO(cors_allowed_origins="*")

def create_app():
    # Chargement des variables d'environnement
    load_dotenv()

    app = Flask(__name__, static_folder='static', static_url_path='/static')

    # Configuration Flask à partir du .env
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")

    # Initialisation extensions
    CORS(app)
    jwt.init_app(app)
    socketio.init_app(app)

    # Connexion à la base de données PostgreSQL
    init_db(app)

    # Enregistrement des blueprints
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(chat_bp, url_prefix="/api/chat")
    app.register_blueprint(match_bp, url_prefix="/api/match")

    return app

# Lancement de l'application
if __name__ == "__main__":
    app = create_app()
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
