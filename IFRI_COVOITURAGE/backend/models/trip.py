class Trip:
    def _init_(self, id, conducteur_id, point_depart, point_arrivee, date_trajet, heure_depart, places_disponibles):
        self.id = id
        self.conducteur_id = conducteur_id
        self.point_depart = point_depart
        self.point_arrivee = point_arrivee
        self.date_trajet = date_trajet
        self.heure_depart = heure_depart
        self.places_disponibles = places_disponibles