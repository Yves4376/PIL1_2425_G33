document.addEventListener("DOMContentLoaded",
function () {
    lottie.loadAnimation({
        container:
        document.getElementById("background-animation"),
        path:"../carpool.json" ,
        renderer: "svg",
        loop: true,
        autoplay:true,
    });
});


fetch('http://localhost:5000/api/login', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));


  fetch("http://localhost:5000/api/register", {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: 'test@gmail.com', password: '1234' })
  })
  .then(res => res.json())
  .then(data => console.log('Réponse:', data))
  .catch(err => console.error('Erreur:', err));


  // Envoi des critères de recherche au backend
async function searchTrips(departureCoords, arrivalCoords, departureTime) {
    const response = await fetch('/api/matching/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${localStorage.getItem('token')}`  // JWT
        },
        body: JSON.stringify({
            departure: departureCoords,
            arrival: arrivalCoords,
            time: departureTime
        })
    });
    return await response.json();
}

// Exemple d'appel depuis le HTML
document.getElementById('search-btn').addEventListener('click', async () => {
    const trips = await searchTrips(
        [6.3725, 2.3580],  // Calavi (exemple)
        [6.3695, 2.3620],  // Campus (exemple)
        "08:00"
    );
    displayTrips(trips);  // Afficher les résultats dans le HTML
});