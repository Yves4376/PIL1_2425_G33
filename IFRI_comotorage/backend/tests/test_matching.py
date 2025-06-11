import unittest
from app import create_app, db
from app.models.user import User
from app.models.trip import Trip
from app.utils.password import hash_password
from app.security.auth import generate_jwt

class MatchingTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()

        # Créer un conducteur
        conducteur = User(
            nom="Marc",
            prenom="Conducteur",
            email="marc@ifri.bj",
            telephone="96000000",
            mot_de_passe=hash_password("1234"),
            role="conducteur"
        )
        db.session.add(conducteur)
        db.session.commit()

        # Créer un trajet
        trajet = Trip(
            conducteur_id=conducteur.id,
            point_depart="Cotonou",
            point_arrivee="IFRI",
            heure_depart="08:00",
            places=3,
            latitude=6.37,
            longitude=2.42
        )
        db.session.add(trajet)
        db.session.commit()

        self.token = generate_jwt(conducteur.id, conducteur.role)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_find_matching(self):
        response = self.client.post("/api/match/find", json={
            "latitude": 6.37,
            "longitude": 2.42,
            "heure": "08:00"
        }, headers={"Authorization": self.token})
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.get_json()) >= 1)

if __name__ == "__main__":
    unittest.main()
