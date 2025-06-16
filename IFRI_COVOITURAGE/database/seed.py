# Importation des modules nécessaires
from flask import Flask, render_template  # Pour créer une app Flask et afficher des templates HTML
import mysql.connector  # Pour se connecter à MySQL depuis Python

# Création de l'application Flask
app = Flask(__name__)

# Configuration de connexion à la base MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'ton_mot_de_passe',  # <-- à adapter
    'database': 'ifri'
}

# Fonction qui initialise la base de données
def init_db():
    # Connexion sans base pour pouvoir la créer
    conn = mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password']
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS ifri")  # Création de la base
    cursor.close()
    conn.close()

    # Connexion à la base nouvellement créée
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Création de la table des utilisateurs
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS utilisateur (
        id INT AUTO_INCREMENT PRIMARY KEY,
        password VARCHAR(128) NOT NULL,
        last_login DATETIME NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        nom VARCHAR(100),
        prenom VARCHAR(100),
        adresse VARCHAR(255),
        is_driver BOOLEAN DEFAULT FALSE,
        is_passenger BOOLEAN DEFAULT TRUE
    )
    """)

    # Création de la table des trajets
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trajet (
        id INT AUTO_INCREMENT PRIMARY KEY,
        conducteur_id INT NOT NULL,
        depart VARCHAR(100) NOT NULL,
        destination VARCHAR(100) NOT NULL,
        date_depart DATE NOT NULL,
        heure_depart TIME NOT NULL,
        places_disponibles INT NOT NULL,
        prix DECIMAL(6,2) DEFAULT 0.00,
        commentaire TEXT,
        FOREIGN KEY (conducteur_id) REFERENCES utilisateur(id) ON DELETE CASCADE
    )
    """)

    # Création de la table des réservations
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reservation (
        id INT AUTO_INCREMENT PRIMARY KEY,
        passager_id INT NOT NULL,
        trajet_id INT NOT NULL,
        date_reservation DATETIME DEFAULT CURRENT_TIMESTAMP,
        places_reservees INT DEFAULT 1,
        statut ENUM('en_attente', 'confirmée', 'annulée') DEFAULT 'en_attente',
        FOREIGN KEY (passager_id) REFERENCES utilisateur(id) ON DELETE CASCADE,
        FOREIGN KEY (trajet_id) REFERENCES trajet(id) ON DELETE CASCADE
    )
    """)

    # Création de la table des avis (feedback)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INT AUTO_INCREMENT PRIMARY KEY,
        reservation_id INT NOT NULL,
        note INT CHECK (note BETWEEN 1 AND 5),
        commentaire TEXT,
        date_feedback DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (reservation_id) REFERENCES reservation(id) ON DELETE CASCADE
    )
    """)

    # On enregistre les modifications
    conn.commit()
    cursor.close()
    conn.close()

# Page d'accueil du site (route "/")
@app.route('/')
def home():
    # Connexion à la base
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)  # Retourne les lignes sous forme de dictionnaire

    # On récupère les 5 prochains trajets
    cursor.execute("SELECT * FROM trajet ORDER BY date_depart LIMIT 5")
    offres = cursor.fetchall()

    # Fermeture de la connexion
    cursor.close()
    conn.close()

    # On passe les trajets à la page HTML
    return render_template('home.html', offres=offres)

# Point d’entrée du programme
if __name__ == '__main__':
    init_db()  # Création des tables à l'exécution
    app.run(debug=True)  # Démarrage du serveur Flask avec mode debug
