from flask import Blueprint, request, jsonify
from security.auth import token_required
from utils.db import get_db
from security.geo_utils import haversine_distance

matching_bp = Blueprint('matching', _name_)

@matching_bp.route('/trips', methods=['POST'])
@token_required
def create_trip(user_id):
    data=request.get_json()
    conn=get_db(); cur=conn.cursor()
    cur.execute("""INSERT INTO rides (conducteur_id,point_depart,point_arrivee,date_trajet,heure_depart,places_disponibles)
                   VALUES(%s,%s,%s,%s,%s,%s)""",
                (user_id,data['point_depart'],data['point_arrivee'],data['date'],data['time'],data['places']))
    conn.commit(); conn.close()
    return jsonify({'message':'Trajet ajouté'})

@matching_bp.route('/match', methods=['POST'])
@token_required
def match(user_id):
    data=request.get_json()
    conn=get_db(); cur=conn.cursor()
    cur.execute("SELECT id,point_depart,point_arrivee,date_trajet,heure_depart FROM rides WHERE date_trajet=%s",
                (data['date'],))
    trips=cur.fetchall(); results=[]
    for t in trips:
        dist = haversine_distance(data['point_depart'], t[1])
        time_diff = abs(datetime.datetime.strptime(data['time'],'%H:%M') -
                        datetime.datetime.combine(t[3], t[4]))
        
        # Simplifié : score = inverse distance/time
        
        score = 1000/(dist+1) + 100/(time_diff.seconds/3600+1)
        results.append({'trip_id':t[0],'score':score})
    results.sort(key=lambda x:x['score'], reverse=True)
    return jsonify(results[:5])