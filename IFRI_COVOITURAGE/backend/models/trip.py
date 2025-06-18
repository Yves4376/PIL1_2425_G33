from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Trip(db.Model):
    _tablename_ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    depart = db.Column(db.String(100), nullable=False)
    destination = db.Column(db.String(100), nullable=False)
    date = db.Column(db.String(20), nullable=False)
    heure = db.Column(db.String(10), nullable=False)
    vehicule = db.Column(db.String(50), nullable=True)
    places = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'depart': self.depart,
            'destination': self.destination,
            'date': self.date,
            'heure': self.heure,
            'vehicule': self.vehicule,
            'places': self.places
        }
from backend import db
class Trip:
    def _init_(self, id, conducteur_id, point_depart, point_arrivee, date_trajet, heure_depart, places_disponibles):
        self.id = id
        self.conducteur_id = conducteur_id
        self.point_depart = point_depart
        self.point_arrivee = point_arrivee
        self.date_trajet = date_trajet
        self.heure_depart = heure_depart
        self.places_disponibles = places_disponibles


