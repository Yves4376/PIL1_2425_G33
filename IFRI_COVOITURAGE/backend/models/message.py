from backend import db
class Message:
    def _init_(self, id, match_id, contenu, expediteur_id, destinataire_id, date_envoi):
        self.id = id
        self.match_id = match_id
        self.contenu = contenu
        self.expediteur_id = expediteur_id
        self.destinataire_id = destinataire_id
        self.date_envoi = date_envoi