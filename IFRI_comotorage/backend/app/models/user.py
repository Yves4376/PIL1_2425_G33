
 #Modéliser les utilisateurs : conducteur ou passager, avec rôles, mot de passe, infos trajets, véhicule, etc.

from app import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    telephone = db.Column(db.String(20), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum('conducteur', 'passager'), nullable=False)

    # Informations de profil
    photo = db.Column(db.String(255))
    vehicule = db.Column(db.String(100))  # Pour les conducteurs
    places_disponibles = db.Column(db.Integer)

    # Localisation (anonymisable)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    # Relations
    trajets = db.relationship("Trip", backref="conducteur", lazy=True)
    messages_envoyes = db.relationship("Message", foreign_keys='Message.expediteur_id', backref='expediteur', lazy=True)
    messages_recus = db.relationship("Message", foreign_keys='Message.destinataire_id', backref='destinataire', lazy=True)

    def __repr__(self):
        return f"<User {self.prenom} {self.nom} ({self.role})>"
