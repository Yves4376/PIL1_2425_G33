from flask import Blueprint, request, jsonify
from flask_socketio import emit
from security.auth import token_required
from utils.db import get_db
from app import socketio

chat_bp = Blueprint('chat', _name_)

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