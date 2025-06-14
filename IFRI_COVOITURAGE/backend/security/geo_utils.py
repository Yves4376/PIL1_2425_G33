import math

def haversine_distance(coord1, coord2):
    """
    Calcule la distance entre deux points géographiques (coord1, coord2)
    exprimés en chaînes "latitude,longitude", en kilomètres.
    """
    try:
        lat1, lon1 = map(float, coord1.split(','))
        lat2, lon2 = map(float, coord2.split(','))
    except ValueError:
        raise ValueError("Les coordonnées doivent être des chaînes 'lat,lon'")

    R = 6371  # Rayon de la Terre en kilomètres

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + \
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * \
        math.sin(dlon / 2) ** 2

    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c

    return round(distance, 2)