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