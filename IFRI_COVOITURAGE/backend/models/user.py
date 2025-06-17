from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    _tablename_ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    is_driver = db.Column(db.Boolean, default=False)  # Pour savoir si c'est un conducteur

    def to_dict(self):
        return {
            'id': self.id,
            'nom': self.nom,
            'email': self.email,
            'is_driver': self.is_driver
        }


from backend import db
class User:
    def _init_(self, id, nom, prenom, email, telephone, mot_de_passe, role):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.mot_de_passe = mot_de_passe
        self.role = role
