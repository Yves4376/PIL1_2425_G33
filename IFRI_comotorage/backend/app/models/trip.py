
 #Modèle pour les trajets publiés (conducteurs et passagers)

from app import db

class Trip(db.Model):
    __tablename__ = 'trips'

    id = db.Column(db.Integer, primary_key=True)
    conducteur_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    point_depart = db.Column(db.String(255), nullable=False)
    point_arrivee = db.Column(db.String(255), nullable=False)
    heure_depart = db.Column(db.Time, nullable=False)
    places = db.Column(db.Integer, nullable=False)

    # Position du point de départ
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __repr__(self):
        return f"<Trip {self.point_depart} -> {self.point_arrivee} à {self.heure_depart}>"

