from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from routes.auth import auth_bp
from routes.chat import chat_bp, db
from routes.matching import matching_bp
from flask_socketio import emit

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
    
    db.init_app(app)