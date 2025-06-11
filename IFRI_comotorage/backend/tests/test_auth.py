import unittest
from app import create_app, db
from app.models.user import User
from flask import json

class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.app_context().push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_register_user(self):
        response = self.client.post("/api/auth/register", json={
            "nom": "Test",
            "prenom": "User",
            "email": "test@ifri.bj",
            "telephone": "90000000",
            "mot_de_passe": "1234",
            "role": "conducteur"
        })
        self.assertEqual(response.status_code, 201)

    def test_login_user(self):
        # D'abord inscription
        self.test_register_user()
        # Puis connexion
        response = self.client.post("/api/auth/login", json={
            "email": "test@ifri.bj",
            "mot_de_passe": "1234"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertIn("token", data)

if __name__ == "__main__":
    unittest.main()
