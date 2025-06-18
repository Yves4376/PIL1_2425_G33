from flask_sqlalchemy import SQLAlchemy
from flask import current_app

db = SQLAlchemy()

def init_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = current_app.config['SQLALCHEMY_DATABASE_URI']
    db.init_app(app)
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas