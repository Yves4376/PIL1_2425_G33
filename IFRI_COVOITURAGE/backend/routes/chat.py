from flask import Blueprint, request, jsonify
from security.auth import token_required
from utils.db import get_db
from app import socketio
from flask_socketio import SocketIO, emit, join_room
from flask import request
from models.user import User

socketio = SocketIO(cors_allowed_origins="*")


chat_bp = Blueprint('chat', __name__)

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    content = data['message']
    user_id = data['user_id']
    emit('message', data, to=room)
    conn = get_db(); cur = conn.cursor()
    cur.execute("INSERT INTO messages (match_id,expediteur_id,destinataire_id,contenu) VALUES(%s,%s,%s,%s)",
                (data['match_id'],user_id,data['dest_id'],content))
    conn.commit(); conn.close()

@chat_bp.route('/history/<int:match_id>', methods=['GET'])
@token_required
def history(user_id, match_id):
    conn=get_db(); cur=conn.cursor()
    cur.execute("SELECT id,expediteur_id,destinataire_id,contenu,date_envoi FROM messages WHERE match_id=%s", (match_id,))
    msgs = cur.fetchall(); conn.close()
    return jsonify([dict(id=row[0],sender=row[1],receiver=row[2],content=row[3],date=row[4].isoformat()) for row in msgs])

@app.route('/api/messages/send', methods=['POST'])
def send_message():
    data = request.get_json()
    sender_id = data.get('sender_id')
    receiver_id = data.get('receiver_id')
    content = data.get('content')

    if not all([sender_id, receiver_id, content]):
        return jsonify({'error': 'Champs manquants'}), 400

    message = Message(sender_id=sender_id, receiver_id=receiver_id, content=content)
    db.session.add(message)
    db.session.commit()

    return jsonify({'message': 'Message envoyé avec succès'}), 201



@app.route('/api/messages/conversation', methods=['GET'])
def get_conversation():
    sender_id = request.args.get('sender_id')
    receiver_id = request.args.get('receiver_id')

    if not sender_id or not receiver_id:
        return jsonify({'error': 'IDs requis'}), 400

    messages = Message.query.filter(
        ((Message.sender_id == sender_id) & (Message.receiver_id == receiver_id)) |
        ((Message.sender_id == receiver_id) & (Message.receiver_id == sender_id))
    ).order_by(Message.timestamp.asc()).all()

    return jsonify([m.to_dict() for m in messages])


@app.route('/api/messages/delete/<int:message_id>', methods=['DELETE'])
def delete_message(message_id):
    message = Message.query.get(message_id)
    if not message:
        return jsonify({'error': 'Message non trouvé'}), 404

    db.session.delete(message)
    db.session.commit()
    return jsonify({'message': 'Message supprimé'})
