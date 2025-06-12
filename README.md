# PIL1_2425_G33
Projet Intégrateur IFRI 2024–2025 : IFRI_comotorage


🚗 IFRI_comotorage – Projet Intégrateur PIL1_2425_33

🎓 Contexte
Dans le cadre du projet intégrateur de fin d’année en Licence 1 à l’Institut de Formation et de Recherche en Informatique (IFRI), il nous a été demandé de concevoir une application web fonctionnelle autour d’un besoin concret.

Le projet IFRI_comotorage a pour objectif de favoriser le covoiturage entre les étudiants de l’IFRI, en leur proposant une plateforme web simple, intuitive et sécurisée.

Ce projet a été réalisé en 4 semaines, en mobilisant nos compétences en développement web, structuration logicielle, sécurité des applications et travail collaboratif.

💡 Présentation de l’application

IFRI_comotorage est une application web qui permet aux étudiants de :

Publier ou rechercher un trajet en covoiturage

Se connecter à un système de messagerie interne

Être mis en relation avec d’autres étudiants selon la proximité géographique et l’horaire souhaité

L’interface utilisateur est claire et moderne grâce à l’intégration de Bootstrap 5, et la communication avec le backend est assurée via des requêtes API en JavaScript.

🔧 Technologies utilisées

Backend : Flask (Python)

Frontend : HTML, CSS, JavaScript, Bootstrap 5

Base de données : MySQL

Authentification : JWT (JSON Web Tokens)

Sécurité : Bcrypt (hachage), AES (chiffrement)

Déploiement : Local (localhost), déployable sur Heroku

🔑 Fonctionnalités principales

Inscription / Connexion sécurisée avec token d’authentification

Publication de trajets par les conducteurs

Recherche intelligente de trajets pour les passagers (par localisation et heure)

Matching automatique via calcul de distance (formule de Haversine)

Profil utilisateur complet avec véhicule, points de départ, etc.

Messagerie interne chiffrée entre utilisateurs

Tableau de bord administrateur via la base de données

⚙️ Installation du projet

Pré-requis
Python ≥ 3.8

MySQL Server

Pip & Virtualenv

Étapes
Créer un environnement virtuel :

Windows :

bash
Copier
Modifier
python -m venv venv
.\venv\Scripts\activate

Linux/macOS :

bash
Copier
Modifier
python3 -m venv venv
source venv/bin/activate


Installer les dépendances :

bash
Copier
Modifier
pip install -r backend/requirements.txt
Configurer la base de données :

Créer une base MySQL nommée ifri_comotorage

Mettre à jour le fichier .env :

ini
Copier
Modifier
SECRET_KEY=ifri_covoit_key
DATABASE_URL=mysql+pymysql://root:motdepasse@localhost/ifri_comotorage
AES_KEY=16bytessecretkey
Initialiser les tables :

bash
Copier
Modifier
cd backend
python run.py
💻 Utilisation de l'application
Côté utilisateur :
Accès au site via index.html

Authentification via formulaire Bootstrap

Publication de trajet pour les conducteurs

Recherche de trajet pour les passagers

Accès au profil utilisateur et messagerie

Côté serveur :
Flask expose des routes API REST sécurisées

Communication avec MySQL via SQLAlchemy

Géolocalisation traitée pour le matching

📁 Structure du projet
pgsql
Copier
Modifier
IFRI_comotorage/
├── backend/
│   ├── app/ (modèles, routes, sécurité)
│   ├── tests/
│   ├── run.py
│   └── requirements.txt
├── frontend/
│   └── public/ (HTML, CSS, JS)
├── database/ (scripts SQL)
├── docs/ (documentation)
├── .env
└── README.md
📦 Déploiement (optionnel)
L’application peut être déployée sur Heroku ou Render :

Ajouter les fichiers :

Procfile

runtime.txt

requirements.txt

Configurer les variables d’environnement en ligne

Lancer :

bash
Copier
Modifier
git push heroku main


Inscription et Connexion
Pour vous inscrire, cliquez sur le bouton "S'inscrire" sur la page d'accueil. Remplissez le formulaire et soumettez-le. Une fois inscrit, utilisez vos identifiants pour vous connecter.

Profil utilisateur
Accédez à votre profil en cliquant sur votre photo de profil en haut à droite. Ici, vous pouvez mettre à jour vos informations personnelles et changer votre photo de profil.

Messagerie instantanée
Accéder à une discussion : Cliquez sur une discussion dans la liste des discussions pour ouvrir la boîte de messagerie.
Envoyer un message : Tapez votre message dans le champ de saisie et cliquez sur "Envoyer".
Liste des discussions
Visualisez toutes vos discussions en cours dans la liste des discussions à gauche. Cliquez sur une discussion pour l'ouvrir.

Suggestions de profils
Découvrez de nouveaux utilisateurs en naviguant dans la rubrique "Suggestions". Utilisez la barre de filtres pour trouver des utilisateurs spécifiques.

Recherche de profils
Recherchez et entamez des discussions en naviguant dans la section "Recherche". Servez vous du filtre pour affiner vos recherches.

Récupération de mot de passe
Cliquez sur le lien <Avez-vous oublié votre mot de passe> sur la page de connexion et recevez un mail de récupération.
