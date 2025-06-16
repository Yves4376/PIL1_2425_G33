from flask import Flask
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
    app.run(debug=True)