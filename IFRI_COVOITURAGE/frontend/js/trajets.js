document.getElementById('searchForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const date = document.getElementById('date').value;
    const heure = document.getElementById('heure').value;
    const depart = document.getElementById('depart').value;
    const destination = document.getElementById('destination').value;
    const token = localStorage.getItem('token');

    try {
        const API_BASE_URL ='http//localhost:5000';
        fetch('${API_BASE_URL}/api/match', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + token
            },
            body: JSON.stringify({
                date: date,
                heure: heure,
                depart: depart,
                destination: destination
            })
        });

        const result = await response.json();
        const resultDiv = document.getElementById('resultatsTrajets');

        if (response.ok) {
            resultDiv.innerHTML = result.length > 0
                ? result.map(trajet => `<p><strong>${trajet.conducteur}</strong> - ${trajet.vehicule} (${trajet.places} places)</p>`).join('')
                : "<p>Aucun trajet trouv .</p>";
        } else {
            resultDiv.innerHTML = `<p class="error-message">${result.message || "Erreur inconnue"}</p>`;
        }

    } catch (error) {
        console.error('Erreur de recherche de trajets:', error);
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