class User:
    def _init_(self, id, nom, prenom, email, telephone, mot_de_passe, role):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.email = email
        self.telephone = telephone
        self.mot_de_passe = mot_de_passe
        self.role = role




"""class User:
    def __init__(self, id, username, email, password, role, photo_url=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.role = role  # "conducteur" ou "passager"
        self.photo_url = photo_url

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "photo_url": self.photo_url
        } """"
