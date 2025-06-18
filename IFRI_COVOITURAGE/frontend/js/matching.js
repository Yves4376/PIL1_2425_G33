// matching.js
document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    const trajetList = document.getElementById('trajetList');

    // Récupérer les trajets disponibles
    fetch('/api/trajets', {
        method: 'GET',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    .then(res => res.json())
    .then(data => {
        if (Array.isArray(data)) {
            data.forEach(trajet => {
                const trajetItem = document.createElement('div');
                trajetItem.className = 'trajet-item';
                trajetItem.innerHTML = `
                    <h3>${trajet.depart}  ${trajet.destination}</h3>
                    <p>Date : ${trajet.date} à ${trajet.heure}</p>
                    <p>Véhicule : ${trajet.vehicule}</p>
                    <p>Places disponibles : ${trajet.places}</p>
                    <button class="reserver-btn" data-id="${trajet.id}">Réserver</button>
                    <hr>
                `;
                trajetList.appendChild(trajetItem);
            });

            // Gestion des boutons "Réserver"
            document.querySelectorAll('.reserver-btn').forEach(button => {
                button.addEventListener('click', () => {
                    const trajetId = button.getAttribute('data-id');
                    reserverTrajet(trajetId, token);
                });
            });
        } else {
            trajetList.innerHTML = '<p>Aucun trajet disponible.</p>';
        }
    })
    .catch(err => {
        console.error('Erreur lors du chargement des trajets', err);
        trajetList.innerHTML = '<p>Erreur lors du chargement.</p>';
    });
});

// Fonction de réservation
function reserverTrajet(trajetId, token) {
    fetch(`/api/reserver/${trajetId}`, {
        method: 'POST',
        headers: {
            'Authorization': 'Bearer ' + token
        }
    })
    .then(res => res.json())
    .then(data => {
        if (data.success) {
            alert('Réservation réussie !');
            location.reload();
        } else {
            alert(data.message || 'Erreur lors de la réservation.');
        }
    })
    .catch(err => {
        console.error('Erreur réservation', err);
        alert('Erreur serveur.');
    });
}


fetch('http://localhost:5000/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));

  function getTrips() {
    fetch('http://localhost:5000/api/trips')
      .then(res => res.json())
      .then(trips => {
        console.log(trips);
        // afficher dans HTML
      });
  }

  
  fetch("http://localhost:5000/api/register", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));