def is_nearby(lat1, lon1, lat2, lon2, threshold_km=1.0):
    from geopy.distance import geodesic
    distance = geodesic((lat1, lon1), (lat2, lon2)).km
    return distance <= threshold_km
