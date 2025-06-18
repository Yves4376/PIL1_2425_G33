from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_bp
from routes.chat import chat_bp, db
from routes.matching import matching_bp
from flask_socketio import emit

from routes.user_routes import user_bp
CORS(app, resources={r"/api/*": {"origins": "*"}})  # À restreindre en production
 
from flask_cors import CORS




app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'votre_clé_secrète'
app.cofig['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:password@localhost/nom_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False



# Enregistrement des blueprints
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(chat_bp, url_prefix='/api')
app.register_blueprint(matching_bp, url_prefix='/api')

if __name__ == '_main_':
   
   
 app.run(debug=True)
    
    
    
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from extensions import db, bcrypt
import os

# Import des routes
from routes.user_routes import user_bp
from routes.trip_routes import trip_bp
from routes.reservation_routes import reservation_bp

app.register_blueprint(user_bp)



jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Configuration depuis les variables d’environnement
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'covoiturage')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'super-secret-key')

    # Initialisation des extensions
    db.init_app(app)
    bcrypt.init_app(app)
    JWTManager(app)
    bcrypt = Bcrypt() # type: ignore
    jwt.init_app(app)
    
    # Enregistrement des routes
    app.register_blueprint(user_bp)
    app.register_blueprint(trip_bp)
    app.register_blueprint(reservation_bp)

    return app

# Point d'entrée
if __name__ == '_main_':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
    
    
from flask import Flask
from extensions import db, cors
from flask_jwt_extended import JWTManager
from routes.auth import auth_bp
from routes.chat import chat_bp
from routes.matching import matching_bp

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost:3306/nom_de_ta_db'
    app.config['JWT_SECRET_KEY'] = 'secret-key'
    
    db.init_app(app)
    JWTManager(app)
    cors.init_app(app)

    # Enregistrement des blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(matching_bp)

    return app

app = create_app()

if __name__ == '_main_':
    app.run(debug=True)    