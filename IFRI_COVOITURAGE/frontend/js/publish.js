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


