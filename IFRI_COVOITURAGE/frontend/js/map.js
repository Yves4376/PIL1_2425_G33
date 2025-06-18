// map.js
document.addEventListener('DOMContentLoaded', () => {
    const map = L.map('map').setView([6.3703, 2.3912], 12); // Ex: Cotonou

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    const points = [
        { lat: 6.3703, lng: 2.3912, label: "Départ" },
        { lat: 6.3603, lng: 2.4000, label: "Destination" }
    ];

    points.forEach(p => {
        L.marker([p.lat, p.lng]).addTo(map)
            .bindPopup(p.label)
            .openPopup();
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


