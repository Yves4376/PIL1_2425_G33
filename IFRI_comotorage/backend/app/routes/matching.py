
 # Matching trajet ↔ passager avec GPS.

from flask import Blueprint, request, jsonify
from app import db
from app.models.trip import Trip
from app.models.user import User
from app.security.auth import token_required
from app.security.geo_utils import haversine

matching_bp = Blueprint("matching", __name__)

@matching_bp.route("/find", methods=["POST"])
@token_required
def find_matching(current_user):
    data = request.get_json()
    lat = data.get("latitude")
    lon = data.get("longitude")
    heure = data.get("heure")

    if not all([lat, lon, heure]):
        return jsonify({'error': 'Latitude, longitude et heure sont requis'}), 400

    trajets = Trip.query.all()
    matches = []

    for trip in trajets:
        distance = haversine(lat, lon, trip.latitude, trip.longitude)
        if distance <= 5 and str(trip.heure_depart) == heure:
            conducteur = trip.conducteur
            matches.append({
                'conducteur': f"{conducteur.nom} {conducteur.prenom}",
                'vehicule': conducteur.vehicule,
                'places': trip.places,
                'heure_depart': str(trip.heure_depart),
                'point_depart': trip.point_depart,
                'point_arrivee': trip.point_arrivee
            })

    return jsonify(matches), 200

