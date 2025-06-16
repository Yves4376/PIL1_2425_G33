from flask import Flask,request,jsonify
from geopy.distance import geodesic
from datetime import datetime

app=Flask(__name__)#base de donnees en mmoire
demandes=[] #lorsque qqun veut prendre ou demander un transport on a ses coordonnees identifiants et heures en temps reels

@app.route('/demande',methods=['POST'])#sert a ajouter une demande

def ajouter_demande():
    data=request.get_json()
    demandes.append(data)
    return jsonify({"message":"DEMANDE AJOUTEE","demande":data})

def heures_compatibles(h1_debut,h1_fin,h2_debut,h2_fin):#pour la compatibilite des heures ou horaires
    debut1=datetime.fromisoformat(h1_debut)
    fin1=datetime.fromisoformat(h1_fin)
    debut2=datetime.fromisoformat(h2_debut)
    fin2=datetime.fromisoformat(h2_fin)
    return max(debut1,debut2)<min(fin1,fin2)

@app.route('/match',methods=['POST'])#recevoir l'offreet return les demandes compatiblrs
def match():
    offre=request.get_json()
    coord_offre=(offre['lng'],offre['lat'])
    matches=[]
    
    for demande in demandes:
        coord_demande=(demande['lng'],demande['lat'])
        distance=geodesic(coord_offre,coord_demande).km
        
        if distance<= 50:#il fallait definir une limite de distance donc j ai pris la plus grande et raisonnable
            if heures_compatibles(offre['heure_debut'],offre['heure_fin'],demande['heure_debut'],demande['heure_fin']):
                matches.append({"demande_id":demande['id'],
                                "distance_km":round(distance,2),
                                "itineraire":f"{coord_offre}{coord_demande}",
                                "lng":demande["lng"],
                                "lat":demande["lat"]})
                return jsonify(matches),200
 
@app.route('/demandes',methods=['GET'])#ceci sert a voir toutes les demandes, c pas necessaire mais j'ai trouvé ca utile
def liste_demandes():
    return jsonify(demandes),200
if __name__=='__main__':
    app.run(debug=True)
                