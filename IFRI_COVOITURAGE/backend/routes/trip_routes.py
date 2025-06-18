@trip_bp.route('/api/trips', methods=['POST'])
@jwt_required()
def create_trip():
    data = request.get_json()
    user_id = get_jwt_identity()
    trip = Trip(
        departure=data['departure'],
        destination=data['destination'],
        date=data['date'],
        user_id=user_id
    )
    db.session.add(trip)
    db.session.commit()
    return jsonify({"message": "Trajet publié"}), 201

@trip_bp.route('/api/trips', methods=['GET'])
def list_trips():
    trips = Trip.query.all()
    results = [{"id": t.id, "departure": t.departure, "destination": t.destination, "date": t.date} for t in trips]
    return jsonify(results)