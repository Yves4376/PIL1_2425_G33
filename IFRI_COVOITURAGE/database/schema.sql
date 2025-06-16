-- TABLE UTILISATEUR (inchangée)
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
);

-- TABLE TRAJET (déjà vue)
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
);

-- TABLE RESERVATION (nouvelle)
CREATE TABLE IF NOT EXISTS reservation (
    id INT AUTO_INCREMENT PRIMARY KEY,
    passager_id INT NOT NULL,
    trajet_id INT NOT NULL,
    date_reservation DATETIME DEFAULT CURRENT_TIMESTAMP,
    places_reservees INT DEFAULT 1,
    statut ENUM('en_attente', 'confirmée', 'annulée') DEFAULT 'en_attente',
    FOREIGN KEY (passager_id) REFERENCES utilisateur(id) ON DELETE CASCADE,
    FOREIGN KEY (trajet_id) REFERENCES trajet(id) ON DELETE CASCADE
);

-- TABLE FEEDBACK (nouvelle)
CREATE TABLE IF NOT EXISTS feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    reservation_id INT NOT NULL,
    note INT CHECK (note BETWEEN 1 AND 5),
    commentaire TEXT,
    date_feedback DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (reservation_id) REFERENCES reservation(id) ON DELETE CASCADE
);
