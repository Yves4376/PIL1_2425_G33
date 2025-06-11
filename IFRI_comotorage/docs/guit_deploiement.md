# Mesures de Sécurité Implémentées

## 1. Hachage des mots de passe
- Algorithme : bcrypt
- Coût : 12 (par défaut)

## 2. Authentification
- JWT avec expiration (1h)
- Clé secrète stockée dans `.env`

## 3. Base de données
- Requêtes paramétrées via SQLAlchemy
- Chiffrement AES pour les numéros de téléphone

## 4. Tests
- Scan OWASP ZAP réalisé le 10/06/2025
- Résultats : Aucune vulnérabilité critique détectée.