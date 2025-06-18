// publish.js
document.getElementById('publishForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const date = document.getElementById('date').value;
    const heure = document.getElementById('heure').value;
    const depart = document.getElementById('depart').value;
    const destination = document.getElementById('destination').value;
    const vehicule = document.getElementById('vehicule').value;
    const places = parseInt(document.getElementById('places').value);
    const token = localStorage.getItem('token');

    try {
        const response = await fetch('/api/trajets', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({
                date,
                heure,
                depart,
                destination,
                vehicule,
                places
            })
        });

        const data = await response.json();

        if (response.ok) {
            alert('Trajet publié avec succès !');
            window.location.href = 'dashboard.html';
        } else {
            alert(data.message || 'Erreur lors de la publication');
        }

    } catch (error) {
        console.error('Erreur publication trajet', error);
    }
});



fetch('http://localhost:5000/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));


  function publishTrip(departure, destination, date) {
    fetch('http://localhost:5000/api/trips', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('token')
      },
      body: JSON.stringify({ departure, destination, date })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
  }

  fetch("http://localhost:5000/api/register", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));

