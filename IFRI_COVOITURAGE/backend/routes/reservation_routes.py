@reservation_bp.route('/api/reservations', methods=['POST'])
@jwt_required()
def reserve_trip():
    data = request.get_json()
    user_id = get_jwt_identity()
    reservation = Reservation(trip_id=data['trip_id'], user_id=user_id)
    db.session.add(reservation)
    db.session.commit()
    return jsonify({"message": "Réservation confirmée"}), 201