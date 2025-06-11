
 # Envoi & lecture des messages.

from flask import Blueprint, request, jsonify
from app import db
from app.models.message import Message
from app.security.auth import token_required

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/send", methods=["POST"])
@token_required
def send(current_user):
    data = request.get_json()
    msg = Message(
        expediteur_id=current_user["user_id"],
        destinataire_id=data["destinataire_id"],
        contenu=data["contenu"]
    )
    db.session.add(msg)
    db.session.commit()
    return jsonify({'message': 'Message envoyé'}), 201

@chat_bp.route("/inbox", methods=["GET"])
@token_required
def inbox(current_user):
    uid = current_user["user_id"]
    messages = Message.query.filter(
        (Message.expediteur_id == uid) | (Message.destinataire_id == uid)
    ).order_by(Message.date_envoi.desc()).all()

    inbox = [{
        'de': m.expediteur.nom,
        'a': m.destinataire.nom,
        'contenu': m.contenu,
        'envoye_le': m.date_envoi.isoformat()
    } for m in messages]

    return jsonify(inbox), 200

