### Application de Covoiturage avec Flask, HTML, CSS et Javascript _ PIL1_2425_G33

   ### Contexte

Chaque année, l'Institut de Formation et de Recherche en Informatique (IFRI) de l'Université d'Abomey-Calavi soumet un défi aux étudiants de Licence 1 en fin d'année. Le projet de cette année consiste à réaliser une application web de covoiturage qui met en relation les étudiants de l'IFRI souhaitant partager leurs trajets quotidiens entre leur domicile et le campus, développée en 2 semaines. Le développement de cette application nous a permis de mettre en œuvre et d'étendre nos connaissances du framework Flask et de sa logique. Le style de l'application a été fait à l'aide de Bootstrap/Tailwind CSS. Afin de la rendre plus facilement testable, le repository contient la base de données, la Secret Key Flask, ainsi que des informations de connexions. Les instructions de déploiement ont été rajoutées un peu plus bas sur le dépôt.
IFRI_covoiturage App







### Fonctionnalités

Inscription et Connexion : Les utilisateurs peuvent s'inscrire et se connecter avec leur email/téléphone pour accéder à la plateforme
Récupération de mot de passe : Les utilisateurs peuvent récupérer leurs mots de passe en cas d'oubli
Profil Utilisateur : Chaque utilisateur a un profil complet avec point de départ, horaires, informations véhicule (conducteur)
Gestion des rôles : Choix et modification du rôle (conducteur ou passager)
Publication d'offres/demandes : Les conducteurs publient des offres, les passagers des demandes de covoiturage
Algorithme de matching intelligent : Mise en correspondance automatique basée sur la proximité géographique et la compatibilité horaire
Messagerie instantanée : Discutez avec d'autres utilisateurs en temps réel pour finaliser les détails du trajet
Historique des conversations : Conservez et parcourez vos conversations précédentes
Interface responsive : Optimisée pour mobiles et adaptée aux tablettes/ordinateurs
Sécurité des données : Authentification sécurisée et protection des données personnelles

### Prérequis
```
Python 3.8+
Flask 2.0+
SQLAlchemy(pour la base de données)
SGBD relationnel (MySQL/PostgreSQL recommandé)
Autres dépendances listées dans requirements.txt
```
### Installation

1. Créer un dossier puis y accéder dans l'éditeur de code
2. Créer et Activer un environnement virtuel

Sous Windows :

```bash 
 python -m venv mon_env
.\mon_env\Scripts\activate
```

Sous Linux :

```bash
python3 -m venv mon_env
source mon_env/bin/activate
```

4. Cloner le dépôt
```bash
(mon_env) https://github.com/Yves4376/PIL1_2425_G33.git
```
6. Naviguer dans le répertoire du projet
```bash
(mon_env) cd PIL1_2425_G33
```

8. Installer les dépendances
```bash
(mon_env) pip install -r requirements.txt
```
9. Configurer la base de données dans le fichier config.py ou app.py
    
### Utilisation de MySQL (recommandé) :

```python
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre-secret-key-ici'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://your_db_user:your_db_password@localhost/ifri_covoiturage_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

7. Initialiser la base de données

```bash
(mon_env) python app.py init-db
```
ou si vous utilisez Flask-Migrate :

```bash
(mon_env) flask db init
(mon_env) flask db migrate -m "Initial migration"
(mon_env) flask db upgrade
8. (Optionnel) Importer des données de test
bash(mon_env) python import_data.py
```
ou
```bash
(mon_env) flask seed-db
```
9. (Optionnel) Créer un utilisateur administrateur
```bash
(mon_env) python create_admin.py
```
11. Démarrer le serveur de développement
```bash
(mon_env) python app.py
```
ou
```bash
(mon_env) flask run
```
L'application sera accessible à l'adresse : http://127.0.0.1:8000/

### Utilisation

L'application IFRI_covoiturage est conçue pour être intuitive et facile d'utilisation.

### Inscription et Connexion*

Pour vous inscrire, cliquez sur le bouton "S'inscrire" sur la page d'accueil. Remplissez le formulaire avec vos informations personnelles (nom, prénom, email, téléphone, mot de passe) et choisissez votre rôle (conducteur ou passager). Une fois inscrit, utilisez vos identifiants (email ou téléphone) pour vous connecter.
Profil Utilisateur
Accédez à votre profil en cliquant sur votre photo de profil en haut à droite. 
Ici, vous pouvez :

Mettre à jour vos informations personnelles
Modifier votre point de départ habituel
Configurer vos horaires de départ/arrivée
Ajouter les informations de votre véhicule (si conducteur)
Changer votre photo de profil
Modifier votre rôle (conducteur/passager)

### Publication d'offres et demandes

 #### Pour les conducteurs :

Accédez à la section "Publier une offre"
Indiquez votre point de départ et d'arrivée
Précisez l'heure de départ et le nombre de places disponibles
Publiez votre offre

#### Pour les passagers :

Accédez à la section "Publier une demande"
Indiquez votre point de départ et d'arrivée souhaités
Précisez l'heure de départ souhaitée
Publiez votre demande

#### Algorithme de matching

Le système propose automatiquement des combinaisons pertinentes basées sur :

La proximité géographique des trajets
La compatibilité des horaires
Les préférences utilisateur

Consultez vos suggestions dans la section "Matches recommandés".

### Messagerie instantanée

Accéder à une conversation : Cliquez sur un utilisateur suggéré ou une conversation existante
Envoyer un message : Tapez votre message dans le champ de saisie et cliquez sur "Envoyer"
Notifications : Recevez des notifications en temps réel pour les nouveaux messages
Historique : Accédez à l'historique de toutes vos conversations

### Recherche et filtres

Utilisez les fonctionnalités de recherche pour :

Trouver des trajets par zone géographique
Filtrer par horaires
Rechercher des utilisateurs spécifiques

#### Structure du projet

```PIL1_2425_G33
IFRI_COVOITURAGE/
│
├── README.md                  # Description complète : projet, installation, usage
├── .gitignore                 # Fichiers/dossiers à ignorer par Git
├── .env.example              # Exemple de configuration d’environnement
├── Dockerfile                 # Image Flask de production
├── docker-compose.yml         # Déploiement : PostgreSQL + Flask
│
├── backend/                   # Code serveur Flask
│   ├── app.py                 # Point d’entrée principal de l’application
│   ├── __init__.py            # Initialise le package Python
│   ├── requirements.txt       # Dépendances du backend
│   ├── static/                # Fichiers statiques (images, CSS partagées, etc.)
│   ├── uploads/               # Uploads des utilisateurs (photos, documents)
│   │
│   ├── models/                # Modèles de base de données
│   │   ├── user.py            # Utilisateur
│   │   ├── trip.py            # Trajet
│   │   └── message.py         # Message / chat
│   │
│   ├── routes/                # Routes Flask organisées
│   │   ├── auth.py            # Authentification : login, register, profil
│   │   ├── chat.py            # Messagerie temps réel
│   │   └── matching.py        # Mise en relation conducteur/passager
│   │
│   ├── security/              # Sécurité et outils sensibles
│   │   ├── auth.py            # JWT, vérification token
│   │   ├── encryption.py      # Hashage mot de passe, tokens de reset
│   │   └── geo_utils.py       # Calcul de distances géographiques
│   │
│   ├── utils/                 # Fonctions utilitaires réutilisables
│   │   ├── db.py              # Connexion PostgreSQL avec dotenv
│   │   └── password.py        # Génération et validation de mots de passe
│   │
│   └── tests/                 # Tests unitaires
│       ├── test_auth.py       # Tests pour auth (login, register, reset)
│       └── test_matching.py   # Tests pour l’algorithme de matching
│
├── database/                  # Base de données
│   ├── schema.sql             # Script SQL de création des tables
│   └── seed.py                # Génération de données de test avec Faker
│
├── frontend/                  # Interface utilisateur (HTML/CSS/JS)
│   ├── index.html             # Page d’accueil
│   ├── login.html             # Connexion utilisateur
│   ├── register.html          # Inscription
│   ├── reset_password.html    # Réinitialisation du mot de passe
│   ├── dashboard.html         # Tableau de bord conducteur/passager
│   │
│   ├── css/
│   │   └── style.css          # Feuille de style principale (responsive)
│   │
│   └── js/                    # Scripts JS côté client
│       ├── auth.js            # Gestion de l'auth via l’API
│       ├── main.js            # Gestion des trajets et matching
│       └── chat.js            # Socket.IO côté client pour la messagerie
│
└── docs/                      # Documentation du projet
    ├── manuel.html            # Guide utilisateur (comment utiliser l’app)
    ├── rapport.html           # Rapport technique complet (structure, BD, sécurité)
    └── postman_collection.json# Collection Postman pour tester les routes API    genere moi le code de chaque partir pour le fonctionnalité de mon application
```

Encadrement pédagogique :

### Supervision : M. Ratheil HOUNDJI
### Encadrants : M. Armand ACCROMBESSI et Mme Maryse GAHOU

### Technologies utilisées

Backend : Python, Flask, SQLAlchemy
Frontend : HTML5, CSS3, JavaScript, Bootstrap/Tailwind CSS
Base de données : MySQL/PostgreSQL
Contrôle de version : Git, GitHub
Algorithme de matching : Calcul de proximité géographique et compatibilité horaire
Templating : Jinja2

### Récupération de mot de passe

Cliquez sur le lien "Mot de passe oublié ?" sur la page de connexion et suivez les instructions pour recevoir un email de récupération.
Interface utilisateur
[Cliquez sur ce lien pour accéder aux captures d'écran de l'interface]

#### Sécurité et confidentialité

Authentification sécurisée avec hashage des mots de passe
Protection des données personnelles selon les standards de sécurité
Confidentialité des localisations (accès restreint aux informations nécessaires)
Validation et assainissement des données d'entrée

### Déploiement

Des instructions détaillées de déploiement sont disponibles dans le fichier DEPLOYMENT.md.
Tests
Pour exécuter les tests :

```bash
(mon_env) python -m pytest tests/
```
ou

```bash
(mon_env) python test_app.py
```
### Contribution

Ce projet est développé dans le cadre du cours "Projet Intégrateur" à l'IFRI. Pour contribuer :

Créez une branche pour votre fonctionnalité
Effectuez vos modifications
Soumettez une pull request

### Licence

Ce projet est développé à des fins éducatives dans le cadre de la formation à l'IFRI - Université d'Abomey-Calavi.

### Université d'Abomey-Calavi
### Institut de Formation et de Recherche en Informatique (IFRI)
### Projet Intégrateur L1 - 2024-2025
