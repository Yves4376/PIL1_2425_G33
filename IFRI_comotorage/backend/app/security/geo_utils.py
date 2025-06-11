
# Outils de localisation (Calcul de distance (Haversine) + anonymisation)


from math import radians, cos, sin, asin, sqrt

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Rayon Terre (km)
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = sin(dlat/2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    return round(R * c, 2)  # Distance en km

def anonymize_coords(lat, lon):
    return round(lat, 2), round(lon, 2)
